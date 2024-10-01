---
title: Writing feeds for fun and nonprofit
draft: true
author: lilly
short_desc: >-
    TODO
tags: [ "blog-meta", "tech" ]
created_at: "2024-10-01 19:15:00+02"
---

What would a blog be without an RSS feed? Or an atom feed?
_It ain't a real one I tell ya!!_
Anyways, so I decided to implement feeeds so that readers can easily subscribe to my amazing content.

## Content

- you need a root `<rss>` tag
- the date format is kinda weird (RFC 822)
- the mail format is weird in the example; i.e. no `name <name@example.com>` but instead `name@example.com (name)`
  the spec doesn't explicity enforce that format though so one can choose
- making the feed discoverable via `<link>`
