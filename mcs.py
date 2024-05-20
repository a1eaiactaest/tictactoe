#!/usr/bin/env python3

from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt

from state import State
from mcts import MCTS


mmap = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
N = int(1e5)
D = 100
initial_state = State([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
heatmap = np.zeros((9))

for _ in trange(N):
    M = MCTS(initial_state)
    best = M.best_action(D)
    heatmap[mmap.index(best)] += 1

heatmap = heatmap.reshape((3, 3))
print(heatmap)
plt.imshow(heatmap)
plt.show()
