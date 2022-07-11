import pandas as pd
import numpy as np
import unittest
import montecarlo

class MontecarloTestSuites(unittest.TestCase):
    def test_1_show_weights(self):
        # test that show_weights shows the die weights
        myDie = montecarlo.Die(np.array(['first', 'second', 'third', 'fourth', 'fifth']))
        
        expected = pd.DataFrame({'faces':['first', 'second', 'third', 'fourth', 'fifth'], 
                                 'weights':[1, 1, 1, 1, 1]})
        check = myDie.show_die().equals(expected)
        self.assertTrue(check)
    def test_2_change_weight(self):
        # change weight and see if it was changed
        myDie = montecarlo.Die(np.array(['first', 'second', 'third', 'fourth', 'fifth']))
        myDie.change_weight('first', 100)
        
        expected = 100
        self.assertEqual(myDie.show_die()['weights'].values[0], expected)
        with self.assertRaises(ValueError):
            myDie.change_weight('whale', 100)
        with self.assertRaises(TypeError):
            myDie.change_weight('first', 'new')
    def test_3_roll(self):
        myDie = montecarlo.Die(np.array(['first', 'second']))
        myDie.change_weight('second', 0)
        roll_1 = myDie.roll()[0]
        self.assertEqual(roll_1, 'first')
    def test_4_play_and_show_results(self):
        unfair_coin = montecarlo.Die(['heads', 'tails'])
        unfair_coin.change_weight('tails', 0)
        unfair_die = montecarlo.Die([1, 2, 3, 4, 5,6])
        unfair_die.change_weight(1, 0)
        unfair_die.change_weight(2, 0)
        unfair_die.change_weight(3, 0)
        unfair_die.change_weight(4, 0)
        unfair_die.change_weight(5, 0)
        myGame = montecarlo.Game([unfair_coin, unfair_die])
        myGame.play(10)
        
        expected = pd.DataFrame([np.repeat('heads', 10), np.repeat(6, 10)]).T
        check = myGame.show_results().equals(expected)
        self.assertTrue(check)
        
        with self.assertRaises(ValueError):
            myGame.show_results('thin')

if __name__ == '__main__':
    unittest.main(verbosity=3)