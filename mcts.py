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
        if self.visits == 0:
            return float("inf")
        return (self.value / self.visits) + 2 * np.sqrt(
            np.log(self.parent.visits) / self.visits
        )


class MCTS:
    def __init__(self, state: State) -> None:
        self.root = Node(state)  # root has no parent

    def best_action(self, simulations_number: int) -> str:
        for _ in range(simulations_number):
            node = self._tree_policy()
            reward = self._default_policy(node.state)
            self._backpropagate(node, reward)
        return self._best_child(self.root, 0).state

    def _tree_policy(self) -> Node:
        node = self.root
        while not node.state.is_game_over()[0]:
            if node.is_leaf():
                return self._expand(node)
            else:
                node = self._best_child(node, 2)
        return node

    def _expand(self, node: Node) -> Node:
        available_moves = node.state.legal_moves()
        random_move = random.choice(available_moves)
        new_state = node.state.apply_move(random_move)
        child_node = Node(new_state, node)
        node.children[random_move] = child_node
        return child_node

    def _best_child(self, node: Node) -> Node:
        return max(node.children.values(), key=lambda child_node: child_node.uct())
