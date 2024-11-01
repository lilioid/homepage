#!/usr/bin/env python3
import argparse
from pathlib import Path

import requests

CSS_DIR = Path(__file__).parent.parent / "src" / "homepage" / "static" / "styles" / "color-schemes"

if __name__ == "__main__":
    argp = argparse.ArgumentParser(prog="get_color_scheme", description="Get a Gogh color scheme and render it as css")
    argp.add_argument("name", help="the name of the scheme (in machine readable form)")
    args = argp.parse_args()

    url = f"https://raw.githubusercontent.com/Gogh-Co/Gogh/refs/heads/master/json/{args.name}.json"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()

    with open(CSS_DIR / f"{args.name}.css", mode="w", encoding="UTF-8") as f:
        f.writelines(
            [
                ":root {\n",
                f"  --color-background: \"{data['background']}\";\n",
                f"  --color-foreground: \"{data['foreground']}\";\n",
                f"  --color-cursor: \"{data['cursor']}\";\n",
                f"  --color-black1: \"{data['color_01']}\";\n",
                f"  --color-black2: \"{data['color_09']}\";\n",
                f"  --color-red1: \"{data['color_02']}\";\n",
                f"  --color-red2: \"{data['color_10']}\";\n",
                f"  --color-green1: \"{data['color_03']}\";\n",
                f"  --color-green2: \"{data['color_11']}\";\n",
                f"  --color-yellow1: \"{data['color_04']}\";\n",
                f"  --color-yellow2: \"{data['color_12']}\";\n",
                f"  --color-blue1: \"{data['color_05']}\";\n",
                f"  --color-blue2: \"{data['color_13']}\";\n",
                f"  --color-magenta1: \"{data['color_06']}\";\n",
                f"  --color-magenta2: \"{data['color_14']}\";\n",
                f"  --color-cyan1: \"{data['color_07']}\";\n",
                f"  --color-cyan2: \"{data['color_15']}\";\n",
                f"  --color-white1: \"{data['color_08']}\";\n",
                f"  --color-white2: \"{data['color_16']}\";\n",
                "}",
            ]
        )
