import unittest
from src.utils.io import readInput
from src.dyn import dyn

class TestDyn(unittest.TestCase):

  def test_ss1(self):
    A, k = readInput("input/ss1.txt")
    sss = dyn(A, k)
    self.assertEqual(k, sss)

  # def test_ss2(self):
  #   A, k = readInput("input/ss2.txt")
  #   sss = dyn(A, k)
  #   self.assertEqual(k, sss)

  # def test_ss3(self):
  #   A, k = readInput("input/ss3.txt")
  #   sss = dyn(A, k)
  #   self.assertEqual(k, sss)

  # def test_ss4(self):
  #   A, k = readInput("input/ss4.txt")
  #   sss = dyn(A, k)
  #   self.assertEqual(k, sss)

  # def test_ss5(self):
  #   A, k = readInput("input/ss5.txt")
  #   sss = dyn(A, k)
  #   self.assertEqual(k, sss)

if __name__ == '__main__':
  unittest.main()