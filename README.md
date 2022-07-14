# game-monte-carlo

# Metadata
Name: Josh Gen

Package: game_monte_carlo

# Synopsis
To install this package, download this repo onto your local machine and run this code in the command line:
```
pip3 install game_monte_carlo
```

Once the package is installed, import the package in python with the following import statement:
```
import game_monte_carlo as mc
```

Once the package is imported you can run any of the three classes created within the montecarlo module - Die, Game, and Analyzer.
An example of creating a die and using each method within the die class is below:
```
sampleDie = mc.Die([1, 2, 3, 4, 5, 6])
sampleDie.change_weights(1, 3)
sampleDie.show_weights()
```

An example of creating a game and using each method within the game class is below:
```
sampleGame = mc.Game(sampleDie, sampleDie, sampleDie)
sampleGame.play(100)
sampleGame.show_results()
```

An example of analyzing a game and using each method within the analyzer class is below:
```
sampleAnalyzer = mc.Analyzer(sampleGame)
sampleAnalyzer.jackpot()
sampleAnalyzer.combo()
sampleAnalyzer.face_counts()
```

# API Description
## Die Class
This class creates a die with weights and allows for changing of those weights as well as rolling of that die.

INPUTS: 
  Faces (numpy array of strings or ints): the names of all the faces of the die
  
### Methods
#### change_weight(face, new_weight):

PURPOSE: Change the weight of a specified face

INPUTS:
  Face (string/int that matches an initialized face): Name of face to change
  New_weight (int/float): New weight to change specified face to
  
OUTPUTS: No outputs


#### roll(rolls=1):

PURPOSE: Roll the die a certain amount of times according to the stored weights

INPUTS: 
  Rolls (int): Number of rolls of the die (OPTIONAL - defaults to 1)

OUTPUTS:
  A list of the results of each roll


#### show_die():

PURPOSE: Show the die's faces and weights

INPUTS: No inputs

OUTPUTS:
  Pandas DataFrame of the die's faces and weights in seperate columns
  
### Attributes
Faces (str or int): List of faces

n (int): Length of faces

Weights (int or float): Weights of each corresponding face (defaults to 1 for each)


## Game Class
This class creates a game in which any number of already specified die are rolled a specified amount of times and resutls can be shown in two different formats.

INPUTS: 
  die_list (list): a list of already initialized die using the Die class.

### Methods

#### play(n_times):

PURPOSE: Roll each of the die a specified number of times

INPUTS: 
  n_times (int): Number of times to roll each die
  
OUTPUTS: No outputs


#### show_results(view="wide"):

PURPOSE: Show the game's results

INPUTS: 
  View (str): Takes two options, wide or narrow, and formats the results accordingly (OPTIONAL - defaults to wide)
                    In wide format, the columns are the die and the rows are the roll numbers
                    In narrow format, the index has both the die and roll number and there is a sole column for face rolled

OUTPUTS:
  Pandas DataFrame of the faces rolled in specified view format

### Attributes
Die_list (list of die objects): List of die objects to be included in the game


## Analyzer Class

PURPOSE: This class takes a game object and performs analyses on it, including number of jackpots, number of unique combinations, and a sparse dataset of counts of each face by roll.

INPUTS: 
  Game object

### Methods

#### jackpot():

PURPOSE:
  Count the amount of jackpots in the game, as defined as when all die in a roll have the same face.

INPUTS: No inputs

OUTPUTS:
  The count of jackpots as an integer
  

#### combo():

PURPOSE:
  Show a table that has the unique counts of each combination of rolls that was rolled.

INPUTS: No inputs

OUTPUTS:
  A dataframe of counts of unique rolls (order does not matter)


#### face_counts():


PURPOSE: Show a table of counts of each face on each roll

INPUTS: No inputs

OUTPUTS:
  A sparse dataframe of counts of each face on each roll
  
### Attributes
game (game object): Game to analyze

game_results (pandas DataFrame): Results of the die game

jackpots_count (int): Count of jackpots from jackpot method

jackpots (pandas DataFrame): A DataFrame of each jackpot

combos (pandas DataFrame): A DataFrame of each unique combination (order does not matter) and their counts

face_counts_per_roll (pandas DataFrame): A sparse DataFrame of counts of each face from each roll

# Manifest

#### git.ignore
This file contains all the file types to ignore in the repo, including DS_Store, .vscode, and others

#### LICENSE
This file contains the internet license for this package

#### README.md
This file describes the important parts of the project and explains each class, method, and attribute in detail

#### montecarlo_tests.py
This file runs tests on the montecarlo module in the game-monte-carlo package

#### montecarlo_tests.txt
This file contains the output of running the montecarlo_tests.py file showing that the tests all passed

#### scenarios.ipynb
This file describes multiple scenarios of using this game ranging from simple coin flipping to word creation with demonstrations of the package's functionality

#### setup.py
This file contains important information for the computer to setup the package using pip install

#### valid_guesses.csv
This is a csv file containing the valid guesses for the popular computer game Wordle and is used in the scenarios.ipynb file

### game_monte_carlo
#### __init__.py
This is the init file in the package that allows the computer to locate the package when pip install is run. This file contains a print statement indicating successful installment and also preloads shortcuts so the import imports the functions directly

#### montecarlo.py
This is the module file which contains the three classes Die, Game, and Analyzer and is the bulk of the project



### Game-MonteCarlo
