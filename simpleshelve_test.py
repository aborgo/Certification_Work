import storescore
import unittest
import os
import shelve
import glob

scoredb = os.getcwd() + '\\scorestore.shlf'

class ScoreTest(unittest.TestCase):

    def test_highscore(self):
        player = 'John'
        scores = [40,30,50,120]
        for i in scores:
            storescore.storescore(player,i)
            shelf = shelve.open(scoredb)
            received = shelf[player]
            shelf.close()
            if i == 30:
                self.assertGreaterEqual(received,i,'nah')
                continue
            self.assertEqual(received,i,'nope')

    def test_many_scores(self):
        HighScore = storescore.storescore
        self.assertEqual(50, HighScore('Kirby', 50))
        self.assertEqual(150, HighScore('Kirby', 150))
        self.assertEqual(150, HighScore('Kirby', 40))
        self.assertEqual(150, HighScore('Kirby', 95))
        self.assertTrue(HighScore('Kirby', 180) == 180, 'Kirby should have 180 as a top score') 

    def testStoreHighScore(self):
        HighScore = storescore.storescore
        self.assertEqual(-100, HighScore('joe', -100))
        self.assertGreater(-99, HighScore('joe', -100))
        self.assertEqual(0, HighScore('joe', 0))
        self.assertLess(0, HighScore('chris', 100))
        self.assertEqual(1000, HighScore('chris', 1000))
        self.assertLess(100, HighScore('chris', 1000))

    def tearDown(self):
        shelve_files = glob.glob(scoredb + '*')
        for fn in shelve_files:
            os.remove(fn)

if __name__ == '__main__':
    unittest.main()
