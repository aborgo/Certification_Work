'''
Created on Nov 4, 2014

@author: aborgo
'''
import unittest
from furnishings import *

class Test(unittest.TestCase):


    def setUp(self):
        self.home = [Bed('Bedroom'),Bookshelf('Bedroom'),Sofa('Living Room')]
        counter(self.home)

    def test_furnishing_map(self):
        observed = map_the_home(self.home)
        expected = {'Bedroom':self.home[0:2], 'Living Room':[self.home[2]]}
        self.assertEqual(observed, expected, 'The mapping is incorrect.')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_furnsihings']
    unittest.main()
