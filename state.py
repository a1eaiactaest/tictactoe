#!/usr/bin/env python3

from typing import Optional


class State:
    """
    state is 9 zeros + 1 zero which tells whose turn it is

    [ 0 0 0 0 0 0 0 0 0 1 ]
    [ a1 a2 a3 b1 b2 b3 c1 c2 c3 current_player]

    because `0` looks like `o` or `O` i'll represent O's as -1 and X's as 1, 0 means empty square
    so the last state digit is for determining whose turn it is, 1 for X and -1 for O
    """

    mmap = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

    def __init__(self, state: list[int]) -> None:
        self.state = state
        self.embed_state = self.state[0:9]
        self.current_player = state[-1] if state else 1

    def legal_moves(self) -> Optional[list[str]]:
        """
        given the current state and the current player (state[-1]),
        return possible moves for that player
        """
        if self.is_game_over()[0]:
            return None
        moves_indicies = []
        for i, j in enumerate(self.embed_state):
            if j == 0:
                moves_indicies.append(i)
        moves = list(map(self.index_to_move, moves_indicies))
        return moves

    def index_to_move(self, index: int) -> str:
        return self.mmap[index]

    def move_to_index(self, move: str) -> int:
        return self.mmap.index(move)

    def apply_move(self, move: str | int) -> "State":
        if isinstance(move, int):
            index = move
        else:
            index = self.move_to_index(move)
        new_state = self.state.copy()
        new_state[index] = self.current_player
        new_state[-1] *= -1  # change player
        return State(new_state)

    # TODO: bench this
    def is_game_over(self) -> tuple[bool, int]:
        """
        if game over
          return (True, -1) if X won , (True, 1) if O, if draw return (True, 0)
        if not game over
          return (False, 0) as nobody has won
        """
        s = self.embed_state
        for turn in [-1, 1]:
            if all(x != 0 for x in s):
                return True, 0
            # check columns
            for i in range(3):
                if all([x == turn for x in [s[i], s[i + 3], s[i + 6]]]):
                    return True, turn
                else:
                    continue
            # check rows
            for i in range(0, 9, 3):
                if all([x == turn for x in s[i : i + 3]]):
                    return True, turn
                else:
                    continue

            # check diagonals
            if all([x == turn for x in [s[0], s[4], s[8]]]):
                return True, turn
            if all([x == turn for x in [s[2], s[4], s[6]]]):
                return True, turn
        return False, self.current_player
