#!/usr/bin/env python3

import unittest
from triplet import Board

class TestGameState(unittest.TestCase):
  def test_over_column(self):
    test_b = Board([1, 0, 0, 1, -1, 0, 1, 0, -1, -1])
    res, _ = test_b.is_game_over()
    self.assertEqual(res, True)
    del test_b, res

  def test_over_row(self):
    test_b = Board([-1, -1, -1, 1, 0, 1, 0, 1, 0, -1])
    res, _ = test_b.is_game_over()
    self.assertEqual(res, True)
    del test_b, res

  def test_over_diagonal(self):
    test_b = Board([-1, 1, 0, 1, -1, 1, 0, 0, -1, -1])
    res, _ = test_b.is_game_over()
    self.assertEqual(res, True)
    del test_b, res
 
  def test_not_over(self):
    test_b = Board([1, 0, 0, 0, -1, 0, 0, 0, 0, 1]) 
    res, _ = test_b.is_game_over()
    self.assertEqual(res, False)
    del test_b, res

  def test_illegal_move(self):
    test_b = Board([0]*9+[1])
    test_b.make_move('a1')
    # Illegal move to occupied square
    _ , res = test_b.make_move('a1')
    self.assertEqual(res, True)
    del test_b, res

  def test_draw(self):
    test_b = Board([-1, -1, 1, 1, 1, -1, -1, 1, 1, -1])
    res, _ = test_b.is_game_over()
    self.assertEqual(res, 'draw')
    del test_b, res

if __name__ == "__main__":
  unittest.main()
