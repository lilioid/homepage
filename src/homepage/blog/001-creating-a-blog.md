---
title: Creating a Blog
author: lilly
short_desc: "A blog post about creating a blog and the technologies used therein"
tags: [ "blog-meta" ]
created_at: "2024-09-24 17:30:00+02"
draft: true
---

Well here we are; the first blog post on this blog.
And it is about the blog itself – kinda self centered but I wanna write down why I did what I did here :)

In creating a blog I wanted to have the following features:

- Easier writing in a markup language other than HTML while keeping a rich featureset such as code blocks and linkable sections
- Automatic article detection from the filesystem
- Automatic generation of index pages that also allow article filtering and maybe even search
- [IndiWeb](https://indieweb.org/) features such as [WebMention](https://indieweb.org/Webmention) and the semantic HTML relevant in that context (See [IndieWeb Building Blocks](https://indieweb.org/Category:building-blocks))
- A link scheme that is flexible and stable


## Markup Language

As a markup language, the choice was not too difficult.
I have written markdown everywhere for quite some time so this was my preferred language.
The implementation I found to be quite useful is [python-markdown](https://python-markdown.github.io/) because the webserver for my homepage is written in python anyway and that library has a stable track record in addition to being quite flexible in terms of markdown extensions[^1][^2].
It is notably not CommonMark but that's okay for me.

The API is also not too difficult to use as you can see by the example below.
I have then also added some extensions for a richer feature-set such as footnotes, code highlighting, tables and other features I just tend to use in other markdown environments.
The rendered `body_html` content is then included in the individual article page via Jinja2.

```python
@dataclass
class Article:
    body: str
    ...

    @property
    def body_html(self) -> str:
        return markdown.markdown(
            text=self.body,
            extensions=[ "fenced_code", "footnotes", "tables", "sane_lists", "smarty", "codehilite" ],
        )
```

## Article Detection

TODO

## Automatic Index Pages

TODO

## IndieWeb

TODO

## Linking Scheme

[^1]: [https://python-markdown.github.io/extensions/](https://python-markdown.github.io/extensions/)
[^2]: [https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions](https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions)
