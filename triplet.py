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

  def legal_moves(self):
    turn = self.state[-1]
    s = self.state[0:9]
    ret = []
    for i, j in enumerate(s):
      if j == 0:
        ret.append(i)
    chret = [self.mb[x] for x in ret]
    return ret, chret

  def is_game_over(self, s=None):
    if s is None:
      s = self.state
    for turn in [-1,1]:
      if all(x!=0 for x in s[0:9]):
        return 'draw', turn
      # check columns 
      for i in range(3):
        if all([x==turn for x in [s[i], s[i+3], s[i+6]]]):
          return True, turn
        else:
          continue

      # check rows
      for i in range(0, 9, 3): 
        if all([x==turn for x in s[i:i+3]]):
          return True, turn
        else:
          continue
      
      # check diagonals
      if all([x==turn for x in [s[0], s[4], s[8]]]):
        return True, turn
      elif all([x==turn for x in [s[2], s[4], s[6]]]):
        return True, turn

    return False, turn

  def make_move(self, move):
    s = self.state
    if type(move) is not int:
      m = self.move_space.get(move)  
    else:
      m = move
    # ILLEGAL MOVE, OPPONENT WINS
    if s[m] != 0:
      self.render_board()
      s[-1] *= -1
      print('Illegal move to %s by %d, %d wins' % (move, s[-1]*-1, s[-1]))
      return s, True 
    if s[-1] == -1:
      s[m] = -1
    elif s[-1] == 1:
      s[m] = 1

    # if -1 change to 1, if 1 change to -1
    self.render_board()
    s[-1] *= -1 
    return s, self.is_game_over()


def random_game(state=None):
  if state == None:
    state = [0]*9+[1]

  b = Board(state)
  done = False
  while not done:
    _, moves = b.legal_moves()
    move = np.random.choice(moves, 1)
    print('\n', move)
    s, (d, w) = b.make_move(move[0])
    print(s,d,w)
    done = d
 
if __name__ == "__main__":
  #random_game()
  b = Board([-1, 1, -1, -1, 1, 0, 1, 1, -1, -1])
  #b = Board([1, 0, 0, 1, -1, 0, 1, 0, -1, -1])
  b.render_board()
  print(b.is_game_over())
