---
title: Building a NOC from scratch
author: lilly
excerpt: >-
  Ich habe dieses Jahr auf dem 39C3 einen Talk über die erste Iteration des Network-Operation-Centers für Europas größte furry-Convention, Euforuence, gehalten. Dieses kleine Team aus dem Chaos, Furries und Chaos-Furries hat ein neues Netzwerk-OC gegründet, um die Eurofurence mit gutem premium 👌 Internetz auszustatten. Ich erzähle von unseren Erfahrungen und den sozialen sowie technischen Herausforderungen.
lang: de
tags: [ "tech", "chaos" ]
created_at: "2025-12-31 18:00:00+02"
draft: false
---
{% from "homepage/macros.html" import command %}

Zum Zeitpunkt der 29. Eurofurence hatte die Eurofurence eine Größe erreicht, bei der typische Event-Locations unsere speziellen Anforderungen nicht mal eben so erfüllen konnten. Beispielsweise ist eine aufwändige Audio/Video-Produktion Teil der Eurofurence, welche ein IP-Netz mit hoher Bandbreite, niederiger Latenz, niedrigem Jitter, Multicast-Transport und präzise Zeitsynchronisierung benötigt. Deshalb wurde dieses Jahr das Onsite Eurofurence Network Operation Center (EFNOC) gegründet. Unsere Aufgabe sollte es sein, alle Anforderungen der anderen Teams kompetent zu erfüllen wovon wir euch in diesem Vortrag etwas aus dem Nähkästchen erzählen wollen.

Grob haben wir wärend der EF29 das Team etabliert und ein Netzwerk gebaut, welches für A/V-Produktion, Event-Koordination und Event-Management (z.B. Security, Ticketing) benutzt wurde. Unser persönliches Ziel war es außerdem, ein benutzbares WLAN-Netzwerk für alle Besuchenden über dies gesamte Event-Venue hinweg zu schaffen – also von Halle H bis zum Vorplatz. Unsere Architektur bestand dafür aus einem simplen Layer2-Netzwerk mit VLAN-Unterteilung, welches von Arista DCS-7050TX-72Q mit 40Gbit/s Optiken bereitgestellt wurde. Die Aristas haben außerdem ein PTP-Signal propagiert, welches von einer Meinberg Master-Clock gesteuert wurde. Zusätzlich war ein Linux-Server als Hypervisor für diverse Netzwerk-Services wie DNS, DHCP, Monitoring und Routing im Einsatz. So zumindest der Plan, denn während des Events wurden wir mit der Realität und vielen „spaßigen“ Problemen konfrontiert.

Der Vortrag beschäftigt sich unter anderem mit diesen Problemen, legt allerdings den Fokus nicht nur auf die technische Darstellung. Stattdessen wird wir auch beleuchtet, wie wir als Team menschlich untereinander und in der Kommunikation mit anderen Teams damit umgegangen sind.

{% call command("xgd-open https://media.ccc.de/v/39c3-building-a-noc-from-scratch", class="not-prose") %}
  <a href="https://media.ccc.de/v/39c3-building-a-noc-from-scratch">Go To Recording</a>
{% endcall %}

