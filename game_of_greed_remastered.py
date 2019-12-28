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
            rounds = 0
            while self.total_score < 10_000 and rounds < 11:
                self._print(f'Starting Round: {rounds}')
                self.total_score += self._turn()
                rounds += 1
            self._print(f'Rounds: {rounds} Final score: {self.total_score}')
        else:
            self._print('OK. Maybe later')

    def _turn(self):
        """
        Method that handles player's turn.
        Turns continue WHILE there are scoring dice from a dice roll.
        Player can reroll or choose to end their turn.
        Returns the turn score.
        """
        turn_score = 0
        dice_aside = ''

# Roll Dice to start the turn ######################################################
        while True:
            current_dice_roll = roll_dice(6 - (len(dice_aside) % 6))
            roll_score = self.calculate_score(current_dice_roll)

# Check for zilch ##################################################################
            if roll_score == 0:
                self._print('ZILCH! Sorry you rolled 0 points. Round over.')
                return 0

# Print the roll ###################################################################
            self._print(current_dice_roll)
            self._print(f'Round Score: {turn_score}')
            self._print(f'Saved Dice: {dice_aside}')
            
# Ask player to set aside ##########################################################
            invalid_response = True
            while invalid_response:
                response = self._input('What dice will you set aside? ')

# check that the player's response is in the current roll ##########################
                if response.isnumeric():
                    mutable_roll = collections.Counter(current_dice_roll)
                    for char in response:
                        if int(char) in mutable_roll and mutable_roll[int(char)] > 0:
                            dice_aside += char
                            mutable_roll[int(char)] -=1
                        else:
                            self._print(f'{response} is an invalid response...')
                            dice_aside = ''
                            continue
                    
                    turn_score += self.calculate_score(dice_aside)
                    invalid_response = False
                else:
                    self._print(f'{response} is an invalid response...')

# let player know where they stand, ask if they want to roll again #################
            if len(dice_aside) == 6:
                self._print(f'SWEEP!! You scored with all six dice! Rolling six again!')
                dice_aside = ''
            else:    
                self._print(f'You entered: {dice_aside}')
                self._print(f'You saved: {turn_score} points')
                response = self._input(f'Roll again? y/n')
            if response == 'n':
                return turn_score

                
                

    def calculate_score(self, current_dice_roll=(2,2,4,4,6,6)):
        """
        Accepts a dice roll as a parameter.
        Returns the calculated score.
        """

        # Cleaning input data for use
        if isinstance(current_dice_roll, str):
            formatted_dice_roll = (int(num) for num in current_dice_roll)    
            distribution_of_dice = collections.Counter(formatted_dice_roll)
        elif isinstance(current_dice_roll, tuple):
            distribution_of_dice = collections.Counter(current_dice_roll)
        else:
            return "Invalid dice roll."

        # Roll Calculation
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
        return roll_score