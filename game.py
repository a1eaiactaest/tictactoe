#!/usr/bin/env python3

from state import State
from mcts import MCTS


initial_state = State([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
M = MCTS(initial_state)
print(M.root)
best = M.best_action(1000)
print(best)
