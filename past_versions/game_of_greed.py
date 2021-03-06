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
    
    def __init__(self, num_rounds=10, print_func=print, input_func=input, do_roll=roll_dice):
        self._print = print_func
        self._input = input_func
        self.total_score = 0
        self.round_score = 0
        self.do_roll = do_roll
        self.current_roll = self.do_roll(6)
        self.current_round = 1
        self.aside = ()
        self.num_rounds = num_rounds
        self.possible_three_pair = []
        self.possible = []
        self.can_reroll = False

    # Handle calculating score for dice roll
    def calculate_score(self, current_dice_roll=(2,2,4,4,6,6)):       
        distribution_of_dice = collections.Counter(current_dice_roll)
        roll_score = 0
        for num in (1,2,3,4,5,6):
            a = '{}{}'.format(num, distribution_of_dice[num])
            if len(self.possible_three_pair) == 3: #three pairs
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

    def play(self):
        """
        Greets user by printing ‘Welcome to Game of Greed’
        Prompts user with ‘Wanna play?’
        Handles the flow of the game
        """
        print_intro_message()

        response = self._input('Wanna play? (y or n):  ')

        if response == 'y':
            self.print_round()
            while self.total_score < 10_000:
                if self.current_roll == ():
                    self._print(' ')
                    self._input(f'SWEEP! You scored with all 6 dice! Rolling 6 new dice... You still have {self.round_score} points set aside!')
                    self.current_roll = self.do_roll(6)
                    self.can_reroll = False
                    # self.print_round()
                    # print_dice(self.current_roll)
                
                # print_dice(self.current_roll)
                if self.calculate_score(self.current_roll) == 0:
                    response = self._input(f'No scoring values... bank your points (currently: {self.round_score}) "b"... or roll again..."r".  ')   
                elif self.aside != ():
                    self.print_round()
                    response = self._input(f'Set your points aside "a"? Or bank what you have (currently: {self.round_score}) "b"? Enter "r" to roll again.')
                else:
                    response = self._input('What will you set aside? Enter a to open up the aside pool.  ')

                if response.lower() == 'r':
                    # self.print_round()
                    if self.can_reroll == False and len(self.current_roll) == 6 and self.calculate_score(self.current_roll) == 0:
                        self.can_reroll = True
                    if self.can_reroll == False:
                        self._print(' ')
                        self._input('You must set aside at least one scoring die each turn... Try again.')
                    if self.can_reroll == True:
                        # self.print_round()
                        self.current_roll = self.do_roll(len(self.current_roll))
                        self.possible_three_pair = []
                        self.possible = []
                        self.can_reroll = False
                        if self.calculate_score(self.current_roll) == 0:
                            self._print(' ')
                            self._input(f'{self.current_roll} Zilch! You rolled no scoring values. You lost your {self.round_score} points set aside. Round {self.current_round} over.')
                            self.aside = ()
                            self.round_score = 0
                            self.current_roll = self.do_roll(6)
                            self.can_reroll = False
                            self.current_round +=1
                            self.print_round()
                        if self.calculate_score(self.current_roll) == 1500:
                            self.round_score += 1500
                            self._print(' ')
                            self.print_round()
                            self._input(f'SWEEP! You scored with all 6 dice! Rolling 6 new dice... You still have {self.round_score} points set aside!')
                            self.current_roll = self.do_roll(6)
                            self.can_reroll = False   
                elif response.lower() == 'quit':
                    break
                elif response.lower() == 'a':
                    self.set_aside(self.current_roll)

                elif response.lower() == 'b':
                    self.can_reroll = False
                    self.bank_dice(self.round_score)
                    self.aside = ()
                    self.round_score = 0
                    self.current_round += 1
                    self.current_roll = self.do_roll(6)
                    self.print_round()
                else:
                    self._print('Please enter r, a, b, or quit')



        # if user enters anything else print ‘OK. Maybe another time’
        else:
            self._print('OK. Maybe another time')
    
    def set_aside(self, current_roll):
        """
        Handles the aside of the game (the dice set aside)
        Prompts the user to select what dice they would like to set aside
        Prompts the user to select how many of those die they would like to set aside
        Conditionals prevent cheating
        """
        # self._print(collections.Counter(current_roll))
        tuples = collections.Counter(current_roll)
        for num in (1,2,3,4,5,6):
            a = '{}{}'.format(num, tuples[num])
            if a[1] == '2':
                self.possible_three_pair.append(a[0])
            if a[0] == '1' and a[1] != '0':
                self.possible.append(a[0])
            elif a[0] == '5' and a[1] != '0':
                self.possible.append(a[0])
            elif a[1] >= '3':
                self.possible.append(a[0])
        print(' '*62)
        while True:
            if len(set(self.possible_three_pair)) == 3:
                self.current_roll = ()
                self.round_score += 1_500
                break        
            response = self._input(f'What will you set aside? {current_roll}  ')
            if response.lower() == 'quit':
                break
            if response in self.possible:
                key_target = response
                value = tuples[int(key_target)]
                print(' '*62)
                response = self._input(f'How many?  ')
                # if key_target != '1' and key_target != '5' and int(response) < 3:
                #     print(' '*62)
                #     response = self._input(f'{key_target} can only be set aside 3 or more... What will you set aside? {current_roll}  ')
                # else:
                if response >= '1' and response <= str(value):
                    new_tuple = ()
                    for i in range(int(response)):
                        new_tuple += (int(key_target),)
                    self.aside += new_tuple
                    self.round_score += self.calculate_score(new_tuple)
                    tuples[int(key_target)] = tuples[int(key_target)] - int(response)
                    self.current_roll = ()
                    for key in tuples:
                        if tuples[key] > 0:
                            for i in range(tuples[key]):
                                self.current_roll += (key,)
                    # self.print_round()
                    self.can_reroll = True
                    break
                else:
                    print(' '*62)
                    response = self._input(f'Please enter a number between 1 and {value}...Select a number to set aside again.  ')
                    # self._print(f'Your current aside pool: {self.aside}')
            else:
                print(' '*62)
                response = self._input(f'Please select a valid die... {current_roll}')   
            

    def bank_dice(self, round_score):
        self.total_score += round_score

    # def print_dice(self):

    def print_round(self):
        self._print(' '*62)
        self._print(' '*62)
        self._print('*'*62)                    
        self._print(f'Round {self.current_round} - - - - - - - - - - - - - - - - - - TOTAL SCORE: {self.total_score}')
        self._print('*'*62)
        print_dice(self.current_roll)
        self._print(' '*62)
        self._print(f'Dice on table: {self.current_roll}')
        self._print(f'Your current aside pool: {self.aside}')        



if __name__ == "__main__":
    game = Game()
    game.play()


