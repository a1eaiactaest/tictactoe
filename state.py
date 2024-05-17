#!/usr/bin/env python3

from typing import Optional

class State:
  '''
  state is 9 zeros + 1 zero which tells whose turn it is

  [ 0 0 0 0 0 0 0 0 0 1 ]
  [ a1 a2 a3 b1 b2 b3 c1 c2 c3 current_player]

  because `0` looks like `o` or `O` i'll represent O's as -1 and X's as 1, 0 means empty square
  so the last state digit is for determining whose turn it is, 1 for X and -1 for O
  '''
  def __init__(self, state:Optional[list[int]]=None) -> None:
    self.state = state
    self.current_player = state[-1] if state else 1

  def legal_moves(self) -> tuple[str]:
    '''
    given the current state and the current player (state[-1]),
    return possible moves for that player
    '''
    raise NotImplementedError
  
  def is_game_over(self) -> tuple[bool, int]:
    '''
    if game over
      return (True, -1) if X won , (True, 1) if O, if draw return (True, 0)
    if not game over
      return (False, 0) as nobody has won
    '''

