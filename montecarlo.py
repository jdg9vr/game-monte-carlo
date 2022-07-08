import pandas as pd
import numpy as np
# REMEMBER TO CHANGE FROM PROTECTED TO PRIVATE
class Die:
    '''
    This class creates a die with weights and allows for changing of those weights as well as
    rolling of that die.
    INPUTS: 
        Faces (numpy array of strings or ints): the names of all the faces of the die
    '''
    def __init__(self, faces):
        self.faces = faces
        self.n = len(faces)
        self.weights = [1 for i in range(self.n)]
        self.__die = pd.DataFrame({'faces':self.faces, 'weights':self.weights})
    def change_weight(self, face, new_weight):
        '''
        PURPOSE:
            Change the weight of a specified face
        INPUTS:
            Face (string/int that matches an initialized face): Name of face to change
            New_weight (int/float): New weight to change specified face to
        OUTPUTS: No outputs
        '''
        if face not in self.__die.faces.values:
            raise ValueError(f"{face} is not in die.")
        elif type(new_weight) != int and type(new_weight) != float:
            raise TypeError("The inputted weight is not a number")
        else:
            self.__die.loc[self.__die.faces==face, 'weights'] = new_weight
    def roll(self, rolls=1):
        '''
        PURPOSE:
            Roll the die a certain amount of times according to the stored weights
        INPUTS: 
            Rolls (int): Number of rolls of the die (OPTIONAL - defaults to 1)
        OUTPUTS:
            A list of the results of each roll
        '''
        return [self.__die.faces.sample(weights=self.__die.weights).values[0] for i in range(rolls)]
    def show_die(self):
        '''
        PURPOSE:
            Show the die's faces and weights
        INPUTS: No inputs
        OUTPUTS:
            Pandas DataFrame of the die's faces and weights in seperate columns
        '''
        return self.__die

myDie = Die(np.array(['first', 'second', 'third', 'fourth', 'fifth']))
myDie.change_weight('first', 'tree')
myDie.change_weight('whale', 3)
myDie.change_weight('second', 100)
myDie.roll(rolls=100)
myDie.show_die()