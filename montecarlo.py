import pandas as pd
import numpy as np
# REMEMBER TO CHANGE FROM PROTECTED TO PRIVATE
# REMEMBER TO ADD DOCSTRINGS
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


class Game:
    '''
    This class creates a game in which any number of already specified die are rolled a specified
    amount of times and resutls can be shown in two different formats.
    INPUTS: 
        die_list (list): a list of already initialized die using the Die class.
    '''
    def __init__(self, die_list):
        self.die_list = die_list
    def play(self, n_times):
        '''
        PURPOSE:
            Roll each of the die a specified number of times
        INPUTS: 
            n_times (int): Number of times to roll each die
        OUTPUTS: No outputs
        '''
        self.__roll_results = pd.DataFrame([die.roll(n_times) for die in self.die_list]).T
        self.__roll_results.index.name = 'roll'
    def show_results(self, view="wide"):
        '''
        PURPOSE:
            Show the game's results
        INPUTS: 
            View (str): Takes two options, wide or narrow, and formats the results accordingly 
                (OPTIONAL - defaults to wide)
                    In wide format, the columns are the die and the rows are the roll numbers
                    In narrow format, the index has both the die and roll number and there is a sole column for face rolled
        OUTPUTS:
            Pandas DataFrame of the faces rolled in specified view format
        '''
        if view == 'wide':
            return self.__roll_results
        elif view == 'narrow':
            return self.__roll_results.stack()
        else:
            raise ValueError("The inputted view format is not applicable, try \"wide\" or \"narrow\"")


class Analyzer:
    '''
    PURPOSE:
        This class takes a game object and performs analyses on it, including number of jackpots,
        number of unique combinations, and a sparse dataset of counts of each face by roll.
    INPUTS:
        Game object
    '''
    def __init__(self, game, n_times):
        self.game = game
        self.game.play(n_times)
        self.game_results = self.game.show_results()
    def jackpot(self):
        '''
        PURPOSE:
            Count the amount of jackpots in the game, as defined as when all die in a roll have the same face.
        INPUTS: No inputs
        OUTPUTS:
            The count of jackpots as an integer
        '''
        self.jackpot_count = 0
        self.jackpots = pd.DataFrame()
        for i in range(len(self.game_results)):
            if len(self.game_results.iloc[i,:].unique()) == 1:
                self.jackpot_count += 1
                self.jackpots = pd.concat([self.jackpots, pd.DataFrame(self.game_results.iloc[i,:]).T])
        return self.jackpot_count
    def combo(self):
        '''
        PURPOSE:
            Show a table that has the unique counts of each combination of rolls that was rolled.
        INPUTS: No inputs
        OUTPUTS:
            A dataframe of counts of unique rolls (order does not matter)
        '''
        self.combos = self.game_results.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('size')
        return self.combos
    def face_counts(self):
        '''
        PURPOSE: Show a table of counts of each face on each roll
        INPUTS: No inputs
        OUTPUTS:
            A sparse dataframe of counts of each face on each roll
        '''
        self.face_counts_per_roll = self.game_results.apply(lambda x: x.value_counts(), 1).fillna(0)
        return self.face_counts_per_roll