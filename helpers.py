#!/usr/bin/env python3

import time
import pstats
import cProfile
import platform
import contextlib
from typing import Optional, Callable


PLAT = platform.system()
assert PLAT == "Darwin" or PLAT == "Linux"


def colored(st: str, color: Optional[str], background: bool = False) -> str:
    if color is not None:
        return f"\u001b[{10*background+60*(color.upper() == color)+30+['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'].index(color.lower())}m{st}\u001b[0m"
    else:
        return st


class Timing(contextlib.ContextDecorator):
    def __init__(
        self, prefix: str = "", on_exit: Optional[Callable] = None, enabled: bool = True
    ) -> None:
        self.prefix = prefix
        self.on_exit = on_exit
        self.enabled = enabled

    def __enter__(self) -> None:
        self.st = time.perf_counter_ns()

    def __exit__(self, *exc):
        et = time.perf_counter_ns()
        self.t = et - self.st
        if self.enabled:
            print(
                f"{self.prefix}{self.t*1e-6:6.2} ms"
                + (self.on_exit(self.t) if self.on_exit else "")
            )


def _format_fcn(fcn) -> str:
    return f"{fcn[0]}:{fcn[1]}:{fcn[2]}"


class Profiling(contextlib.ContextDecorator):
    def __init__(
        self,
        enabled: bool = True,
        sort: str = "cumtime",
        frac: float = 0.2,
        fn: Optional[str] = None,
        ts: int = 1,
    ) -> None:
        self.enabled = enabled
        self.sort = sort
        self.frac = frac
        self.fn = fn
        self.time_scale = 1e3 / ts

    def __enter__(self) -> None:
        self.pr = cProfile.Profile()
        if self.enabled:
            self.pr.enable()

    def __exit__(self, *exc) -> None:
        if self.enabled:
            self.pr.disable()
            if self.fn:
                self.pr.dump_stats(self.fn)
            stats = pstats.Stats(self.pr).strip_dirs().sort_stats(self.sort)
            for fcn in stats.fcn_list[0 : int(len(stats.fcn_list) * self.frac)]:
                (_, num_calls, tottime, cumtime, callers) = stats.stats[fcn]
                scallers = sorted(callers.items(), key=lambda x: -x[1][2])
                print(
                    f"n:{num_calls:8d}  tm:{tottime*self.time_scale:7.2f}ms  tot:{cumtime*self.time_scale:7.2f}ms",
                    colored(_format_fcn(fcn), "yellow")
                    + " " * (50 - len(_format_fcn(fcn))),
                    colored(
                        f"<- {(scallers[0][1][2]/tottime)*100:3.0f}% {_format_fcn(scallers[0][0])}",
                        "BLACK",
                    )
                    if len(scallers)
                    else "",
                )
