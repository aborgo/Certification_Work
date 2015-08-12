'''
Created on Dec 17, 2014

@author: aborgo
'''
import unittest
from sstr import sstr

class Test(unittest.TestCase):
    
    def test_sstr(self):
        s1 = sstr("abcde")
        self.assertEqual(s1 >> 0, sstr("abcde"))
        self.assertEqual(s1 << 0, sstr("abcde"))
        self.assertEqual(s1 << 2,sstr("cdeab"))
        self.assertEqual(s1 >> 2,sstr("deabc"))
        self.assertEqual(s1 >> 5,sstr("abcde"))
        self.assertTrue((s1 >> 5) << 5 == sstr("abcde"))
        s2 = sstr("abcdefghijlkmnopqrst")
        self.assertEqual(s2>>10, sstr("lkmnopqrstabcdefghij"))
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_sstr']
    unittest.main()
