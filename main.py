#!/usr/bin/env python3

"""

a kirdengarten implementation of tictactoe in python written while listening to great music

"""
from math import sqrt
import numpy as np

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
    self.state = [0]*9+[-1]
    
  # return state in 2d
  def render_board(self):
    print("turn: %d" % self.state[-1])
    print(np.array(self.state[0:9]).reshape(3,3)) 

  def make_move(self, move=None):
    m = self.move_space.get(move)  
    if self.state[-1] == -1:
      self.state[m] = 1
    elif self.state[-1] == 1:
      self.state[m] = -1

    # if -1 change to 1, if 1 change to -1
    self.state[-1] *= -1 
    self.render_board()
    return self.state
       
    
    
if __name__ == "__main__":
  b = Board() 
  print(b.make_move('a1'))
  print(b.make_move('b1'))
  print(b.make_move('b2'))
