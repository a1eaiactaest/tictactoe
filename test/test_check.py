#!/usr/bin/env python3

import unittest
from triplet import Board

class TestGameState(unittest.TestCase):
  def test_over(self):
    test_b = Board([1, 0, 0, 1, -1, 0, 1, 0, -1, -1])
    res, _ = test_b.is_game_over()
    self.assertEqual(res, True)
    del test_b, res
 
  def test_not_over(self):
    test_b = Board([1, 0, 0, 0, -1, 0, 0, 0, 0, 1]) 
    res, _ = test_b.is_game_over()
    self.assertEqual(res, False)
    del test_b, res

  def test_draw(self):
    pass

if __name__ == "__main__":
  unittest.main()
