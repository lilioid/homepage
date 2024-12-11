import random
from typing import Any

from fastapi import Request

MSGS = [
    "Du bist die Brandmauer gegen Rechts",
    "„Unpolitisch“ ist politisch",
    "Die AfD ist die mit Abstand größte Gefahr für unsere Gesellschaft! #AfDVerbotJetzt",
    "Sich an Antifaschismus stören ist so 1933",
    "Diese Website wird nicht von Faschisten betrieben",
    "Menschenrechte statt rechte Menschen",
    "Kein Mensch ist illegal",
    "„Nie wieder“ ist immer, nicht nur alle 4 Jahre beim Kreuzchen machen",
    "Kein Platz für Rassismus",
    "Trans rights are human rights",
    "Trans rights or riot nights",
    "AfDler verpisst euch – keiner vermisst euch",
    "Seenotrettung ist kein Verbrechen",
]


def context_processor(_r: Request) -> dict[str, Any]:
    return {
        "antinazi_message": random.choice(MSGS),
    }
