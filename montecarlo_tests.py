import pandas as pd
import numpy as np
import unittest
import montecarlo
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

class MontecarloTestSuites(unittest.TestCase):
    def test_1_show_weights(self):
        # test that show_weights shows the die weights
        myDie = Die(np.array(['first', 'second', 'third', 'fourth', 'fifth']))
        
        expected = pd.DataFrame({'faces':['first', 'second', 'third', 'fourth', 'fifth'], 
                                 'weights':[1, 1, 1, 1, 1]})
        check = myDie.show_die().equals(expected)
        self.assertTrue(check)
    def test_2_change_weight(self):
        # change weight and see if it was changed
        myDie = Die(np.array(['first', 'second', 'third', 'fourth', 'fifth']))
        myDie.change_weight('first', 100)
        
        expected = 100
        self.assertEqual(myDie.show_die()['weights'].values[0], expected)
        with self.assertRaises(ValueError):
            myDie.change_weight('whale', 100)
        with self.assertRaises(TypeError):
            myDie.change_weight('first', 'new')
    def test_3_roll(self):
        myDie = Die(np.array(['first', 'second']))
        myDie.change_weight('second', 0)
        roll_1 = myDie.roll()[0]
        self.assertEqual(roll_1, 'first')
    def test_4_play_and_show_results(self):
        unfair_coin = Die(['heads', 'tails'])
        unfair_coin.change_weight('tails', 0)
        unfair_die = Die([1, 2, 3, 4, 5,6])
        unfair_die.change_weight(1, 0)
        unfair_die.change_weight(2, 0)
        unfair_die.change_weight(3, 0)
        unfair_die.change_weight(4, 0)
        unfair_die.change_weight(5, 0)
        myGame = Game([unfair_coin, unfair_die])
        myGame.play(10)
        
        expected = pd.DataFrame([np.repeat('heads', 10), np.repeat(6, 10)]).T
        check = myGame.show_results().equals(expected)
        self.assertTrue(check)
        
        with self.assertRaises(ValueError):
            myGame.show_results('thin')
    def test_5_jackpot(self):
        unfair_die = Die([1, 2, 3, 4, 5, 6])
        unfair_die.change_weight(1, 0)
        unfair_die.change_weight(2, 0)
        unfair_die.change_weight(3, 0)
        unfair_die.change_weight(4, 0)
        unfair_die.change_weight(5, 0)
        unfair_die2 = Die([1, 2, 3, 4, 5, 6])
        unfair_die2.change_weight(1, 0)
        unfair_die2.change_weight(2, 0)
        unfair_die2.change_weight(3, 0)
        unfair_die2.change_weight(4, 0)
        unfair_die2.change_weight(6, 0)
        myGameDie = Game([unfair_die, unfair_die2])
        myGameDie.play(10)
        dieAnalysis = Analyzer(myGameDie, 100)
        check = dieAnalysis.jackpot()==0
        self.assertTrue(check)
    def test_6_jackpots(self):
        fair_die = Die([1, 2, 3, 4, 5, 6])
        unfair_die = Die([1, 2, 3, 4, 5, 6])
        unfair_die.change_weight(1, 0)
        unfair_die.change_weight(2, 0)
        unfair_die.change_weight(3, 0)
        unfair_die.change_weight(4, 0)
        unfair_die.change_weight(5, 0)
        kinda_fair_die = Die([1, 2, 3, 4, 5, 6])
        kinda_fair_die.change_weight(1, 2)
        kinda_fair_die.change_weight(3, 2)
        kinda_fair_die.change_weight(6, 2)
        myGameDie = Game([fair_die, unfair_die, kinda_fair_die])
        myGameDie.play(10)
        dieAnalysis = Analyzer(myGameDie, 1000)
        dieAnalysis.jackpot()
        check = dieAnalysis.jackpots.apply(lambda x: len(x.unique())-1, 1).sum() == 0
        self.assertTrue(check)
    def test_7_combo(self):
        fair_die = Die([1, 2, 3, 4, 5, 6])
        unfair_die = Die([1, 2, 3, 4, 5, 6])
        unfair_die.change_weight(1, 0)
        unfair_die.change_weight(2, 0)
        unfair_die.change_weight(3, 0)
        unfair_die.change_weight(4, 0)
        unfair_die.change_weight(5, 0)
        kinda_fair_die = Die([1, 2, 3, 4, 5, 6])
        kinda_fair_die.change_weight(1, 2)
        kinda_fair_die.change_weight(3, 2)
        kinda_fair_die.change_weight(6, 2)
        myGameDie = Game([fair_die, unfair_die, kinda_fair_die])
        myGameDie.play(10)
        dieAnalysis = Analyzer(myGameDie, 1000)
        self.assertTrue(isinstance(dieAnalysis.combo().index, pd.MultiIndex))
    def test_8_face_counts(self):
        unfair_die = Die([1, 2, 3, 4, 5, 6])
        unfair_die.change_weight(1, 0)
        unfair_die.change_weight(2, 0)
        unfair_die.change_weight(3, 0)
        unfair_die.change_weight(4, 0)
        unfair_die.change_weight(5, 0)
        unfair_die2 = Die([1, 2, 3, 4, 5, 6])
        unfair_die2.change_weight(1, 0)
        unfair_die2.change_weight(2, 0)
        unfair_die2.change_weight(3, 0)
        unfair_die2.change_weight(4, 0)
        unfair_die2.change_weight(6, 0)
        game_dies = [unfair_die, unfair_die2]
        myGameDie = Game(game_dies)
        myGameDie.play(10)
        n = 100
        dieAnalysis = Analyzer(myGameDie, n)
        check = dieAnalysis.face_counts().shape == (n, len(game_dies))
        self.assertTrue(check)
        

if __name__ == '__main__':
    unittest.main(verbosity=3)