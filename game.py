#!/usr/bin/env python3
import numpy as np

from triplet import Board


def random_game(state=None) -> None:
    if state is None:
        state = [0] * 9 + [1]

    b = Board(state)
    b.render_board()
    print(b.is_game_over())
    print(b.legal_moves())
    done = False
    while not done:
        _, moves = b.legal_moves()
        print(moves)
        move = np.random.choice(1, moves)
        print("\n", move)
        s, (d, w) = b.make_move(move[0])
        print(s, d, w)
        done = d


if __name__ == "__main__":
    random_game()
