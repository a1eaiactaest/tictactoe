#!/usr/bin/env python3

import numpy as np
from typing import Optional
from state import State

class Node:
  def __init__(self, state: State):
    self.state: State = state
    self.parent: Node = None
    self.children = {}
    self.visits = 0
    self.value = 0

  def is_leaf(self) -> bool:
    return (len(self.children) == 0)

  @property
  def uct(self) -> float:
    return self.value + 2 * np.sqrt(np.log(self.parent.visits) / self.visits)