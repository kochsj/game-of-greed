import collections
import random
from dice_art import print_dice, dice_art, print_intro_message

def roll_dice(number_of_dice):
    """
    This method generates a dice roll using the number_of_dice available.
    It generates random numbers (dice rolls between 1 and 6) for each die that is rolled.
    Returns the current_dice_roll property of roll_dice; a tuple of the dice roll values.
    """
    return tuple(random.randint(1,6) for _ in range(number_of_dice)) 

class Game:
    """
    Instanciates a game of greed!
    Methods prompt the player, roll dice, calculate score, and keep track of the flow of the game.
    """
    def __init__(self, _print=print, _input=input):
        self.total_score = 0

        self._input = _input
        self._print = _print

    def play(self):
        """
        Greets user by printing ‘Welcome to Game of Greed’
        Prompts user with ‘Wanna play?’
        Handles the flow of the game
        """
        self._print('Welcome to Game of Greed')
        response = self._input('Wanna play? ')
        if response == 'y':
            pass
        else:
            self._print('OK. Maybe later')
            
    # Handle calculating score for dice roll
    def calculate_score(self, current_dice_roll=(2,2,4,4,6,6)):      
        distribution_of_dice = collections.Counter(current_dice_roll)
        roll_score = 0
        for num in (1,2,3,4,5,6):
            a = '{}{}'.format(num, distribution_of_dice[num])
            if len(current_dice_roll) == 6 and set(distribution_of_dice.values()) == {2}: #three pairs
                roll_score += 1500
                return roll_score
            if len(distribution_of_dice) == 6: #straight • six/six unique numbers
                roll_score += 1500
                return roll_score
            if len(distribution_of_dice.values()) == 3 and set(distribution_of_dice.values()) == {2}: # three pairs
                roll_score += 1500
                return roll_score              
            elif a[0] == '1': # ones
                if a[1] < '3':
                    roll_score += 100*int(a[1])
                else:
                    roll_score += 1000*(int(a[1])-2)
            elif a[0] == '5': # fives
                if a[1] >= '3':
                    roll_score += 100*int(a[0])*(int(a[1])-2)
                else:    
                    roll_score += 50*int(a[1])
            elif a[1] >= '3': # 3 or more of a kind
                roll_score += 100*int(a[0])*(int(a[1])-2)
        # The output from calculate_score is an integer representing the roll’s score according to rules of game.
        return roll_score