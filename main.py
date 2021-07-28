#!/usr/bin/env python3

"""

a kirdengarten implementation of tictactoe in python written while listening to great music

"""
from math import sqrt

board = [0,0,0,0,0,0,0,0,0]


class Board():
  def __init__(self, state=None):
    if state is None:
      self.reset_state()
    else:
      self.state = state

  def reset_state(self):
    self.state = [0]*10
    
  def display(self, arr:'list', space:'int') -> 'list':
    key = int(sqrt(space))
    for i in range(0, space, key):
      print(arr[i:i+key])


if __name__ == "__main__":
  b = Board()
  print(b.state)
