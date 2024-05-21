#!/usr/bin/env python3

import platform
from typing import Optional


PLAT = platform.system()
assert PLAT == "Darwin" or PLAT == "Linux"


def colored(st: str, color: Optional[str], background=False) -> str:
    if color is not None:
        return f"\u001b[{10*background+60*(color.upper() == color)+30+['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'].index(color.lower())}m{st}\u001b[0m"
    else:
        return st
