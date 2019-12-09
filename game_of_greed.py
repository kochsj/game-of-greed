import collections
# Today is all about tackling the highest risk features - scoring and the game flow.
# Define a Game class.

class GameOfGreed:
    
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func

# Handle calculating score for dice roll
    def calculate_score(self, current_dice_roll=(1,5,5,2,4,5)):       
        distribution_of_dice = collections.Counter(current_dice_roll)
        roll_score = 0
        for num in (1,2,3,4,5,6):
            a = '{}{}'.format(num, distribution_of_dice[num])
            if len(distribution_of_dice) == 6: #straight • six/six unique numbers
                print('1500')
                return 1_500
            elif a[0] == '1':
                roll_score += 100*int(a[1])
            elif a[0] == '5':
                roll_score += 50*int(a[1])
            elif a[1] >= '3':
                roll_score += 100*int(a[1])
# The output from calculate_score is an integer representing the roll’s score according to rules of game.
        self._print(roll_score)
        return roll_score


# Add play instance method to Game class
    def play(self, response=None):
        # Greet user by printing ‘Welcome to Game of Greed’
        self._print('Welcome to Game of Greed')

       
        if response == None:
            return

        # if user enters ‘y’ then print ‘Great! Check back tomorrow :D’
        if response == 'y':
            self._print('Great! Check back tomorrow :D')

        # if user enters anything else print ‘OK. Maybe another time’
        else:
            self._print('OK. Maybe another time')



if __name__ == "__main__":
    game = GameOfGreed()
    game.play(input('Wanna play?'))

