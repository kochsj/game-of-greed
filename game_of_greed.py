import collections
import random
# Today is all about tackling the highest risk features - scoring and the game flow.
# Define a Game class.

class GameOfGreed:
    
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func
        self.total_score = 0
        self.current_roll = ()
        self.current_round = 1
        self.aside = ()

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
        # self._print('Welcome to Game of Greed')
        print_intro_message()
        # Prompt user with ‘Wanna play?’
        response = self._input('Wanna play? (y or n):  ')

        if response == 'y' or user_response == 'y':
            self.current_roll = self.roll_dice(6)
            self._print(self.current_roll)
            while True:
                if self.calculate_score(self.current_roll) == 0:
                    response = self._input('Too bad! Roll Again... Enter "r".  ')
                elif self.aside != ():
                    response = self._input('Set your points aside? Or bank what you have? Enter "b" to bank. Enter "r" to roll again. set aside.  ')
                else:
                    response = self._input('What will you set aside? Enter a to open up the aside pool.  ')

                if response.lower() == 'r':
                    pass
                elif response.lower() == 'quit':
                    break
                elif response.lower() == 'a':
                    self.set_aside(self.current_roll)
                elif response.lower() == 'b':
                    pass
                else:
                    self._print('Please enter r, a, b, or quit')



        # if user enters anything else print ‘OK. Maybe another time’
        else:
            self._print('OK. Maybe another time')

    def roll_dice(self, number_of_dice):
        current_dice_roll = ()
        for i in range(number_of_dice):
            current_dice_roll += ((random.randint(1,6)),)
        return current_dice_roll    
    
    def set_aside(self, current_roll):
        self._print(f'Your current aside pool: {self.aside}')
        # self._print(collections.Counter(current_roll))
        tuples = collections.Counter(current_roll)
        possible = []
        for num in (1,2,3,4,5,6):
            a = '{}{}'.format(num, tuples[num])
            if a[0] == '1' and a[1] != 0:
                possible.append(a[0])
            elif a[0] == '5' and a[1] != 0:
                possible.append(a[0])
            elif a[1] >= '3':
                possible.append(a[0])
        response = self._input(f'What will you set aside? {current_roll}')
        while True:
            if response in possible:
                key_target = response
                value = tuples[int(key_target)]
                response = self._input(f'How many?')
                self._print(response)
                if response >= '1' and response <= str(value):
                    new_tuple = ()
                    for i in range(int(response)):
                        new_tuple += (key_target,)
                    self.aside += new_tuple
                    tuples[int(key_target)] = tuples[int(key_target)] - int(response)
                    print(f'should be less: {tuples[int(key_target)]}')
                    self.current_roll = ()
                    for key in tuples:
                        if tuples[key] > 0:
                            for i in range(tuples[key]):
                                self.current_roll += (key,)
                    break
                else:
                    response = self._input(f'Please enter a number between 1 and {value}...Select a number to set aside again.')
                    self._print(f'Your current aside pool: {self.aside}')
            else:
                response = self._input(f'Please select a valid die...')   
            

    def bank_dice(self, aside):
        aside_total = self.calculate_score(aside)
        self.total_score += aside_total

def print_intro_message():
    print(' '*4, '*'*62)
    print(' '*4, '*'*62)
    print(' '*4, '*'*5, ' '*50, '*'*5)
    print(' '*4, '*'*5, ' '*8, '~ WELCOME TO THE GAME OF GREED ~', ' '*8, '*'*5)
    print(' '*4, '*'*5, ' '*50, '*'*5)
    print(' '*4, '*'*5, ' '*50, '*'*5)
    print(' '*4, '*'*5, ' '*10, 'Dice rolling, game of chance!', ' '*9, '*'*5)
    print(' '*4, '*'*5, ' '*10, 'First to 10,000 points wins!', ' '*10, '*'*5)
    print(' '*4, '*'*5, ' '*7, 'Prompts will ask you to roll dice,', ' '*7, '*'*5)
    print(' '*4, '*'*5, ' '*7, 'set dice aside, or bank dice. Ones', ' '*7, '*'*5)
    print(' '*4, '*'*5, ' '*7, 'and Fives are always worth points.', ' '*7, '*'*5)
    print(' '*4, '*'*5, ' '*6, 'Triples, quads, straights worth more.', ' '*5, '*'*5)
    print(' '*4, '*'*5, ' '*50, '*'*5)
    print(' '*4, '*'*5, ' '*50, '*'*5)
    print(' '*4, '*'*5, ' '*8, 'For complete rules, please visit:', ' '*7, '*'*5)
    print(' '*4, '*'*5, ' '*4, 'https://en.wikipedia.org/wiki/Dice_10000', ' '*4, '*'*5)    
    print(' '*4, '*'*5, ' '*9, 'Follow prompts to get started.', ' '*9, '*'*5)  
    print(' '*4, '*'*5, ' '*8, "Type 'quit' at any time to exit.", ' '*8, '*'*5)
    print(' '*4, '*'*5, ' '*50, '*'*5)
    print(' '*4, '*'*62)
    print(' '*4, '*'*62, end="\n"*3)


if __name__ == "__main__":
    game = GameOfGreed()
    game.play()


# - [x] Application should implement features from class 1
# - [x] Application should have unit tests to ensure proper operation
# - [x] Application should simulate rolling between 1 and 6 dice



# - [x] Application should allow user to set aside dice each roll

# - [x] Application should allow “banking” current score or rolling again.

# - [x] Application should keep track of total score
            #self.total_score
# Application should keep track of current round
    #self.current_round
