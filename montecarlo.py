import pandas as pd
import numpy as np
# REMEMBER TO CHANGE FROM PROTECTED TO PRIVATE
# ADD DOCSTRINGS
class Die:
    def __init__(self, faces):
        self.faces = faces
        self.n = len(faces)
        self.weights = [1 for i in range(self.n)]
        self._die = pd.DataFrame({'faces':self.faces, 'weights':self.weights})
    def change_weight(self, face, new_weight):
        if face not in self._die.faces.values:
            raise ValueError(f"{face} is not in die.")
        elif type(new_weight) != int and type(new_weight) != float:
            raise TypeError("The inputted weight is not a number")
        else:
            self._die.loc[self._die.faces==face, 'weights'] = new_weight
    def roll(self, rolls=1):
        return [self._die.faces.sample(weights=self._die.weights).values[0] for i in rolls]

myDie = Die(np.array(['first', 'second', 'third', 'fourth', 'fifth']))
myDie.change_weight('first', 'tree')
myDie.change_weight('second', 3)
myDie._die.faces.sample(weights=myDie._die.weights).values[0]