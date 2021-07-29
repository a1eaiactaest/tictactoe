#!/usr/bin/env python3

"""

a kirdengarten implementation of tictactoe in python written while listening to great music

"""
import os
from math import sqrt
import numpy as np

DEBUG = os.getenv("DEBUG", None) is not None

# assume that board is always 3x3
class Board():
  mb = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
  def __init__(self, state=None):
    if state is None:
      self.reset_state()
    else:
      self.state = state
    self.move_space = dict((m,n) for n,m in enumerate(self.mb))

  def reset_state(self):
    if DEBUG:
      self.state = [i for i in range(9)]+[1]
    else:
      self.state = [0]*9+[1]
    
  # return state in 2d
  def render_board(self):
    print("turn: %d" % self.state[-1])
    print(np.array(self.state[0:9]).reshape(3,3)) 

  def is_game_over(self, s=None):
    if s is None:
      s = self.state
    if all(x!=0 for x in s[0:9]):
      return 'draw', s[-1]
    # check columns 
    for i in range(3):
      ret = 0 
      for j in range(0, 9, 3):
        if s[j] == s[-1]*-1:
          ret += 1
      if ret == 3:
        return True, s[-1]
      else:
        continue
    #return False, self.state[-1]

    # check rows
    for i in range(0, 9, 3): 
      #print([x for x in s[i:i+3]])
      if all([x==s[-1] for x in s[i:i+3]]):
        return True, s[-1] 
      else:
        continue
    
    # check diagonals
    if all([x==s[-1] for x in [s[0], s[4], s[8]]]):
      return True, s[-1]
    elif all([x==s[-1] for x in [s[2], s[4], s[6]]]):
      return True, s[-1]

    return False, s[-1]

  def make_move(self, move):
    m = self.move_space.get(move)  
    if self.state[-1] == -1:
      self.state[m] = -1
    elif self.state[-1] == 1:
      self.state[m] = 1

    # if -1 change to 1, if 1 change to -1
    self.state[-1] *= -1 
    self.render_board()
    print(self.is_game_over(self.state))
    return self.state
 
if __name__ == "__main__":
  #test_state = [0]*9+[1]
  test_state = [-1,1,0,1,-1,1,0,0,-1,-1]
  b = Board(test_state)
  b.render_board()
  print(b.is_game_over())
