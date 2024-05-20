#!/usr/bin/env python3

import random
import numpy as np

from state import State


class Node:
    def __init__(self, state: State, parent: "Node" = None):
        self.state: State = state
        self.parent: Node = parent
        self.children = {}
        self.visits = 0
        self.value = 0

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def uct(self) -> float:
        return self.value + 2 * np.sqrt(np.log(self.parent.visits) / self.visits)
