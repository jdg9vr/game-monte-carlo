"""
This file initializes the package when pip install is run. It preloads the Die, Game, and Analyzer functions and prints package loaded so the user knows the init file was run.
"""
from .montecarlo import Die
from .montecarlo import Game
from .montecarlo import Analyzer
print('Montecarlo game loaded!')
