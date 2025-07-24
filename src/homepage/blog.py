import logging
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path as FsPath
from typing import List, Optional, Self

import frontmatter
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger(__name__)


@dataclass
class Post:
    """Metadata and content for each blog post"""

    id: int
    title: str
    excerpt: str
    tags: List[str]
    created_at: datetime
    edited_at: Optional[datetime]
    author: str
    is_draft: bool
    is_outdated: bool
    lang: str
    raw_body: str

    @property
    def ref(self) -> str:
        name = self.title.lower().replace(" ", "-").replace("/", "-").replace("&", "and")
        return f"{self.id:03}-{name}"

    @property
    def last_modified(self) -> datetime:
        if self.edited_at is not None:
            return self.edited_at
        return self.created_at

    @property
    def reading_time(self) -> int:
        # https://www.readingtimeestimator.com/
        match self.lang:
            case "de":
                chars_per_minute = 978
            case _other:
                chars_per_minute = 987

        return round(len(self.raw_body) / chars_per_minute)

    @classmethod
    def read_from_path(cls, path: FsPath) -> Self:
        """Read the given files content and extract post metadata + content from it"""
        logger.info("Reading post from path %s", path)

        with path.open("r", encoding="utf-8") as f:
            fm = frontmatter.load(f)

        return Post(
            id=extract_post_id(path.name),
            title=str(fm["title"]),
            excerpt=str(fm["excerpt"]),
            tags=list(fm["tags"]),
            created_at=datetime.fromisoformat(str(fm["created_at"])),
            edited_at=datetime.fromisoformat(str(fm["edited_at"])) if "edited_at" in fm else None,
            author=str(fm["author"]),
            is_draft="draft" in fm and fm["draft"] is True,
            is_outdated="outdated" in fm and fm["outdated"] is True,
            lang=str(fm["lang"]),
            raw_body=fm.content,
        )


def extract_post_id(article_ref: str) -> int:
    """Extract an articles numeric ID from a given reference"""
    return int(re.match(r"(\d+)(-.*)?", article_ref).group(1))


class BlogCollection:
    CACHE_KEY = "homepage.blog.collection"
    posts = List[Post]

    def __init__(self, posts: List[Post]):
        self.posts = list(sorted(posts, key=lambda post: post.created_at, reverse=True))

    @classmethod
    def get_instance(cls) -> Self:
        instance = cache.get(cls.CACHE_KEY)
        if instance is not None:
            return instance

        instance = cls.construct_from_source(settings.BASE_DIR / "src" / "homepage" / "blog")
        cache.set(cls.CACHE_KEY, instance)
        return instance

    @classmethod
    def construct_from_source(cls, path: FsPath) -> Self:
        logger.info("Reading blog collection from source at %s", path)
        posts = [
            Post.read_from_path(dir_path / file_path)
            for (dir_path, _dir_names, file_names) in path.walk()
            for file_path in file_names
            if file_path.endswith(".md")
        ]
        return cls(posts)

    def __iter__(self):
        return iter(self.posts)
