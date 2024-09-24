from dataclasses import dataclass
from typing import Any

from fastapi import Request


@dataclass(frozen=True)
class Friend:
    name: str
    url: str


FRIENDS = [
    Friend(name="bonsaibeef.de", url="https://bonsaibeef.de/"),
    Friend(name="Freddy", url="https://frederico.info/"),
    Friend(name="Helena", url="https://helena.place/"),
    Friend(name="kritzl", url="https://kritzl.dev/"),
    Friend(name="Noah Fust", url="https://noahfuhst.de/"),
    Friend(name="olebit", url="https://oleb.it/"),
    Friend(name="traumweh", url="https://traumweh.dev/"),
    Friend(name="Vic Wrobel", url="https://www.vicwrobel.de/"),
]


def context_processor(_r: Request) -> dict[str, Any]:
    return {
        "friends": FRIENDS,
    }
