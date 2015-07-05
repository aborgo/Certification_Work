"""
performs simple tests of composable functions.
"""
import unittest
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing."
    return s[::-1]

def square(x):
    "Multiplies a number by itself."
    return x*x


class ComposableTestCase(unittest.TestCase):

    def test_inverse(self):
        reverser = Composable(reverse)
        nulltran = reverser * reverser
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(nulltran(s), s)
            
    def test_inverse2(self):
        reverser = Composable(reverse)
        nulltran = reverser ** 2
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(nulltran(s), s)
    
    def test_square(self):
        squarer = Composable(square)
        po4 = squarer * square
        for v, r in ((1, 1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)
            
    def test_power(self):
        powers = Composable(square)
        po4 = powers**2
        for v, r in ((1, 1), (2, 2**4), (3, 3**4)):
            self.assertEqual(po4(v), r)
            
    def test_exceptions(self):
        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc
        with self.assertRaises(TypeError):
            fc = fc**'not an integer'
        with self.assertRaises(ValueError):
            fc = fc**-5

if __name__ == "__main__":
    unittest.main()

