#!/usr/bin/env python3

"""

a kirdengarten implementation of tictactoe in python written while listening to great music

"""
from math import sqrt

board = [0,0,0,0,0,0,0,0,0]

class Board:
  def __init__(self, state):
    pass 

def display(arr:'list', n:'int') -> 'list':
  key = int(sqrt(n))
  for i in range(0, n, key):
    #print(i)
    print(arr[i:i+key])

display(board, len(board))
