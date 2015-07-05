"""
Created by Adam Borgo

Math quiz with timer.
"""

from datetime import datetime
from random import randint


def _print(phrase):
    'Hides print while run in the test'
    if __name__ == '__main__':
        print(phrase)

class Quiz:

    def questions(self):
        'asks questions and creates attributes for generated questions'
        global count
        count = 0
        for n in range(5):
            first_number = randint(1,10)
            second_number = randint(1,10) 
            correct = first_number + second_number 
            time1 = datetime.now()
            while True:
                try:
                    inp = int(input('{} + {} = ?'.format(first_number, second_number)))
                    break
                except ValueError:
                    continue
            time2 = datetime.now()
            elapsed = int((time2 - time1).total_seconds())
            if inp == correct:
                answer = 'right'
            else:
                answer = 'wrong'
            _print('{} is {}!'.format(inp,answer))
            self.__dict__.update({'question{}'.format(n+1):(n+1, elapsed,answer)})

        
    def results(self):
        'prints out formatted results'
        qlist = ['question1','question2','question3','question4','question5']
        total = 0
        for i in qlist:
            q = getattr(self,i)
            question_number, elapsed,answer = q
            total += elapsed
            msg = 'Question #{} took about {} second(s) to complete and was {}.'
            msg = msg.format(question_number, elapsed, answer)
            _print(msg)
        average = total/5
        msg = 'You took {} second(s) to finish the quiz'.format(total)
        _print(msg)
        msg = 'Your average time was {} second(s) per question'.format(average)
        _print(msg)
        
        
if __name__ == '__main__':
    a = Quiz()
    a.questions()
    a.results()

