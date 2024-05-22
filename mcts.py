#!/usr/bin/env python3

import math
import random
from typing import Optional

from state import State


class Node:
    def __init__(self, state: State, parent: Optional["Node"] = None):
        self.state = state
        self.parent = parent
        self.children = {}
        self.visits = 0
        self.value = 0

        self.uct = float("inf")

        # prevent division by zero, is this the right fix?
        if self.parent is not None and self.parent.visits == 0:
            self.parent.visits = 1

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def update_uct(self) -> None:
        if self.visits == 0:
            self.uct = float("inf")
        elif self.parent is None:
            self.uct = float("inf")
        else:
            self.uct = (self.value / self.visits) + 2 * math.sqrt(
                math.log(self.parent.visits) / self.visits
            )

    def add_child(self, move: str, child_node: "Node") -> None:
        self.children[move] = child_node
        child_node.parent = self


class MCTS:
    def __init__(self, state: State) -> None:
        self.root = Node(state)  # root has no parent

    def best_action(self, simulations_number: int) -> str:
        for _ in range(simulations_number):
            node = self._tree_policy()
            reward = self._default_policy(node.state)
            self._backpropagate(node, reward)
        return self._best_child(self.root)

    def _tree_policy(self) -> Node:
        node = self.root
        while not node.state.is_game_over()[0]:
            if node.is_leaf():
                return self._expand(node)
            else:
                node = node.children[self._best_child(node)]
        return node

    def _expand(self, node: Node) -> Node:
        available_moves = node.state.legal_moves()
        if available_moves is None:
            return node
        random_move = random.choice(available_moves)
        new_state = node.state.apply_move(random_move)
        child_node = Node(new_state, node)
        node.children[random_move] = child_node
        return child_node

    def _best_child(self, node: Node) -> str:
        return max(node.children, key=lambda k: node.children[k].uct())

    def _default_policy(self, state: State) -> int:
        current_state = state
        while not current_state.is_game_over()[0]:
            available_moves = current_state.legal_moves()
            if available_moves is None:
                return state.state[-1]
            random_move = random.choice(available_moves)
            current_state = current_state.apply_move(random_move)
        return current_state.is_game_over()[1]

    def _backpropagate(self, node: Node, reward: int) -> None:
        while node is not None and node.parent is not None:
            node.visits += 1
            node.value += reward
            node = node.parent
            reward *= -1
