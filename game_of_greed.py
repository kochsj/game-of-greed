import collections
# Today is all about tackling the highest risk features - scoring and the game flow.
# Define a Game class.

class GameOfGreed:
    
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func

# Handle calculating score for dice roll
    def calculate_score(self, current_dice_roll=(2,2,4,4,6,6)):       
        distribution_of_dice = collections.Counter(current_dice_roll)
        roll_score = 0
        for num in (1,2,3,4,5,6):
            a = '{}{}'.format(num, distribution_of_dice[num])
            if len(distribution_of_dice) == 6: #straight • six/six unique numbers
                roll_score += 1500
                return roll_score
            if len(distribution_of_dice.values()) == 3 and set(distribution_of_dice.values()) == {2}:
                roll_score += 1500
                return roll_score              
            elif a[0] == '1':
                if a[1] < '3':
                    roll_score += 100*int(a[1])
                else:
                    roll_score += 1000*(int(a[1])-2)
            elif a[0] == '5':
                if a[1] >= '3':
                    roll_score += 100*int(a[0])*(int(a[1])-2)
                else:    
                    roll_score += 50*int(a[1])
            elif a[1] >= '3':
                roll_score += 100*int(a[0])*(int(a[1])-2)
# The output from calculate_score is an integer representing the roll’s score according to rules of game.
        return roll_score


# Begin work on verifying the game proceeds according to game flow
# Ensure that the initial game flow is followed
# Add play instance method to Game class
# NOTE: use Dependency Injection to handle input/output.
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

if __name__ == "__main__":
    game = GameOfGreed()

    game.calculate_score()

