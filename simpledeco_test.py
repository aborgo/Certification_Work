import unittest
from addarg import *

class Test_AddArg(unittest.TestCase):
    def test_decorator(self):
        @addarg(1)
        def prargs(*args):
            return args
        observed = prargs(2, 3)
        expected = (1, 2, 3)
        self.assertEqual(observed, expected)
        observed = prargs("child") 
        expected = (1, 'child')
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    unittest.main()
