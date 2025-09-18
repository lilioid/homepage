---
title: Encrypted Ceph in Proxmox
author: lilly
excerpt: >
  Sometimes, you are in the situation to run proxmox with Ceph, still want your data encrypted but don't feel like setting up an encrypted root partition.
  This small writeup explains how one can encrypt their Ceph-OSDs without storing the encryption key in plaintext.
lang: en
tags: [ tech, proxmox ]
created_at: "2025-09-18 18:20:00+02"
draft: True
---

I was recently in the situation where I had a [Proxmox PVE Cluster](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) set up with its [Ceph](https://ceph.io/en/) integration enabled.
I also wanted to properly encrypt my data at rest.

One thing I wanted to avoid here was setting up a whole encrypted root partition because that involves typing in the encryption key during the boot procedure.
This can be done either physically – <span class="text-yellow1">*ughhh please no!*</span> – or by inserting a small SSH server into the [initramfs](https://en.wikipedia.org/wiki/Initial_ramdisk) of the linux boot process.
This can actually also be a bit painful to get right and I didn't feel like building that setup either.

## My Technical Premise

I had the following Proxmox setup.
This guide can probably be adopted to other environments if you know what you're doing but this is the environment in which I built it.

- Proxmox PVE 9.0.10
- ZFS for the root partition and main proxmox system
- A separate partition which the [Ceph OSD](https://docs.ceph.com/en/latest/glossary/#term-Ceph-OSD) is managing.
  [Encryption](https://docs.ceph.com/en/latest/radosgw/encryption/) is turned on.

## How Encryption works in Ceph

The [Ceph Encryption Documentation](https://docs.ceph.com/en/latest/radosgw/encryption/) gives an overview about how encryption in Ceph generally works.

The important part is that in modern setups, the Ceph OSD can simply have its encryption flag turned on.
If this is the case, the OSD will set itself up to run on a [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup) encrypted block device.
Key management for that LUKS device is completely transparent and done by Ceph on its own.
The OSD sends over all key material to the [Ceph Mon](https://docs.ceph.com/en/latest/glossary/#term-Ceph-Monitor) daemons and fetches it again on startup.

This makes things easier in traditional ceph operations where one may have a large amount of Ceph OSDs and a small, trusted and secured Ceph management plane.
When using Ceph with Proxmox as part of a [Hyper-Converged Ceph Cluster](https://pve.proxmox.com/wiki/Deploy_Hyper-Converged_Ceph_Cluster) however, MON daemons probably run on the same nodes as OSDs.
This makes just OSD encryption pretty pointless since the required key material is just stored one partition over as part of the MON database :(

## A simple ZFS based solution

Since Proxmox is using Debian as a base, standard Debian solutions (SystemD in this case) can be employed.
The idea is that I am storing all MON data in an encrypted [ZFS dataset](https://openzfs.github.io/openzfs-docs/man/master/7/zfsconcepts.7.html) that is not required to be unlocked for boot.
So a separate one than the root partition and with a key managed by me!

1. First, the dataset must be created.
   I used the following command:

```text
zfs create -o mountpoint=/var/lib/ceph/mon -o encryption=on -o keylocation=prompt -o keyformat=passphrase rpool/ceph-mon
```

2. Then, a Ceph Mon can be created.
   This can be done through any of the ways documented the [Proxmox Ceph Docs](https://pve.proxmox.com/wiki/Deploy_Hyper-Converged_Ceph_Cluster#pve_ceph_monitors) or however you like.
   By default, Ceph stores Mon data in `/var/lib/ceph/mon/` so right where the ZFS dataset is mounted.

3. As an additional safeguard, ensure that Ceph Mons are only started when the dataset is mounted.
   This can be done by defining a [SystemD Drop-In](https://man.archlinux.org/man/systemd.unit.5) for the `ceph-mon@.service` unit.

    Just run `systemctl edit ceph-mon@.service` from a shell on the proxmox node and enter the following content:

```text
# /etc/systemd/system/ceph-mon@.service.d/override.conf
[Unit]
AssertPathIsMountPoint=/var/lib/ceph/mon/
```

## Node Startup Procedure

Now, because of the steps above, the proxmox node does not boot up 100% on its own any more.
But this was more or less the point :)

To complete a node's boot procedure, I now need to <q>load the encryption key</q> for ZFS and then tell it to actually mount the dataset:
```shell
zfs mount -l rpool/ceph-mon
```

Afterwards, MON daemons can be started again:
```shell
systemctl start ceph-mon@pve1
```
