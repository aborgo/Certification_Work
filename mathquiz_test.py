import unittest
import re
import time
from unittest.mock import patch
import mathquiz

def adder(phrase):
    """Mock function that mimics user input"""
    
    regex = re.compile(r'\s\d\d*|\d\d*\s')
    matches = regex.findall(phrase)
    numbers = []
    for i in matches:
        i = i.strip()
        i = int(i)
        numbers.append(i)
    inp1,inp2 = numbers
    while mathquiz.count < 2:
        mathquiz.count += 1
        time.sleep(1)
        return 3745
    time.sleep(1)
    return inp1 + inp2


class test_mathquiz(unittest.TestCase):
    
    
    @patch('builtins.input',adder)
    def test_quiz(self):
        a = mathquiz.Quiz()
        a.questions()
        self.assertEqual(a.question1,(1,1,'wrong'))
        self.assertEqual(a.question2,(2,1,'wrong'))
        self.assertEqual(a.question3,(3,1,'right'))
        self.assertEqual(a.question4,(4,1,'right'))
        self.assertEqual(a.question5,(5,1,'right'))

        
        
        
if __name__ == '__main__':
    unittest.main()
