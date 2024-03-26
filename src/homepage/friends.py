from dataclasses import dataclass
from typing import Any

from fastapi import Request


@dataclass(frozen=True)
class Friend:
    name: str
    url: str


FRIENDS = [
    Friend(name="Noah Fust", url="https://noahfuhst.de/"),
    Friend(name="Vic Wrobel", url="https://www.vicwrobel.de/"),
    Friend(name="bonsaibeef.de", url="https://bonsaibeef.de/"),
    Friend(name="kritzl", url="https://kritzl.dev/"),
    Friend(name="olebit", url="https://oleb.it/"),
    Friend(name="traumweh", url="https://traumweh.dev/"),
]


def context_processor(_r: Request) -> dict[str, Any]:
    return {
        "friends": FRIENDS,
    }
