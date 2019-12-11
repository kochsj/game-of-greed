import collections
import random
# Today is all about tackling the highest risk features - scoring and the game flow.
# Define a Game class.

class GameOfGreed:
    
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func
        self.total_score = 0
        self.current_round = 1

    # Handle calculating score for dice roll
    def calculate_score(self, current_dice_roll=(2,2,4,4,6,6)):       
        distribution_of_dice = collections.Counter(current_dice_roll)
        roll_score = 0
        for num in (1,2,3,4,5,6):
            a = '{}{}'.format(num, distribution_of_dice[num])
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

    def play(self, user_response=None):
        # Greet user by printing ‘Welcome to Game of Greed’
        self._print('Welcome to Game of Greed')

        # Prompt user with ‘Wanna play?’
        response = self._input('Wanna play?')

        # if user enters ‘y’ then print ‘Great! Check back tomorrow :D’
        if response == 'y' or user_response == 'y':
            self._print('Great! Check back tomorrow :D')

        # if user enters anything else print ‘OK. Maybe another time’
        else:
            self._print('OK. Maybe another time')

    def roll_dice(self, number_of_dice):
        current_dice_roll = ()
        for i in range(number_of_dice):
            current_dice_roll = current_dice_roll + ((random.randint(0,6)),)
        return current_dice_roll    
    
    def set_aside_dice(self):
        pass

    def bank_dice(self):
        pass
if __name__ == "__main__":
    game = GameOfGreed()
    game.play()

# - [x] Application should implement features from class 1
# - [x] Application should have unit tests to ensure proper operation
# Application should simulate rolling between 1 and 6 dice

# Application should allow user to set aside dice each roll

# Application should allow “banking” current score or rolling again.



# Application should keep track of total score
    #self.total_score
# Application should keep track of current round
    #self.current_round