from collections import Counter
import random
from dice_art import print_dice, dice_art, print_intro_message

def roll_dice(number_of_dice):
    """
    This method generates a dice roll using the number_of_dice available.
    It generates random numbers (dice rolls between 1 and 6) for each die that is rolled.
    Returns the current_dice_roll property of roll_dice; a tuple of the dice roll values.
    """
    return tuple(random.randint(1,6) for _ in range(number_of_dice)) # returns a tuple (#,#,#,#,#,#)

def calculate_score(dice_roll):
    """
    Calculate score takes in a dice roll
    Calculates the highest possible accumulative score
    Returns roll_score
    """
    distribution_of_dice = Counter(dice_roll)
    roll_score = 0
    if len(distribution_of_dice) == 3 and set(distribution_of_dice.values()) == {2}: #### three pairs
        roll_score += 1500
        return roll_score
    if distribution_of_dice[1] == 2 and distribution_of_dice[5] == 4: ### 2 ones and 4 fives
        roll_score += 2_200
        return roll_score
    if len(distribution_of_dice) == 6: #straight • six/six unique numbers
        roll_score += 1500
        return roll_score
    if distribution_of_dice[1] > 0: #ones
        if distribution_of_dice[1] < 3:
            roll_score += 100*distribution_of_dice[1]
        else: 
            roll_score += 1000 * (distribution_of_dice[1]-2)
    if distribution_of_dice[5] > 0: #fives
        if distribution_of_dice[5] < 3:
            roll_score += 50*distribution_of_dice[5]
        else:
            roll_score += 500*(distribution_of_dice[5]-2)
    for num in distribution_of_dice:
        if num != 1 and num != 5 and distribution_of_dice[num] >= 3: # 3 or more of a kind Not including ones and fives
            roll_score += 100*(num)*(distribution_of_dice[num]-2)                  
    return roll_score

class GameOfGreed:

    def __init__(self, num_rounds=10, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func
        self._rounds = num_rounds
        self.current_round = 1
        self.current_dice_roll = ()
        self.current_aside_pool = ()
        self.total_score = 0
        self.round_score = 0

    def __repr__(self):
        return "A Game of Greed"

    def play(self):
        """
        Greets user by printing ‘Welcome to Game of Greed’
        Prompts user with ‘Wanna play?’
        Handles the flow of the game
        """
        print_intro_message() # 1 # print intro

        response = self._input('Wanna play? (y or n):  ') # 2 # prompt user

        if response.lower() == 'y': # 3 # Conditional to check if user would like to play
            while self.current_round <= self._rounds: # 4 # while there are still rounds to play...
                # 5 # take a turn - roll, aside, banking, sweeping, zilching,
                self.take_a_turn(6)
                # 6 # add to round count
                self.current_round += 1
            self._print(f'Final Score: {self.total_score}. Thanks for playing!') # 7 # print final score when there are no more rounds

        else: # 3(cont.) # If user does not want to play
            self._print('Ok. Maybe another time')


    def take_a_turn(self, number_of_dice):
        while True:
        # 1 # Roll the dice - add them to self.current dice pool
            self.current_dice_roll = roll_dice(number_of_dice)
        # 2 # print current round to the screen
            print(self.current_dice_roll)
        # 3 # calculate the score
            # if the score is 0, prints zilch and round ends
            if calculate_score(self.current_dice_roll) == 0:
                self._print(f'{self.current_dice_roll} Zilch! You rolled no scoring values. You lost your {self.round_score} points set aside. Round {self.current_round} over.')
                self.current_aside_pool = ()
                self.round_score = 0
                return
            #otherwise continue
            else: #as long as there are scoring dice
            #   on every roll I want user to be prompted to set something aside
                response = self._input('What will you set aside? ')
                response = self.set_aside(response)    
            #   after set aside i want user to have the option to bank or reroll or set more aside (if more are able to be set aside).
                if calc == 0:
                    response = self._input(f'You have no more scoring dice, enter "r" to roll again. Type "b" to bank what you have (currently: {self.round_score}). ')
                else: # otherwise roll again or bank 
                    response = self._input(f'Set more scoring dice aside or enter "r" to roll again. Type "b" to bank what you have (currently: {self.round_score}). ')
                if response == 'b':
                    self.bank_dice()
                    return # end the round on bank
                if response == 'r':
                    self.round_score += calculate_score(self.current_aside_pool)
                    self.current_aside_pool = ()
                    roll = self.do_reroll()
                    take_a_turn(roll)
                # if response == #is a number, check if it can be set aside
                if response.lower() == 'quit':
                    break

        # 4 # Think about the score (conditionals) and Make a decision:
                #4a# prompt the user "What do you want to set aside? Or will you bank your points? Or roll again and risk them all??"
                    # 4a # Set Aside ()
                    # 4b # Bank
                    # 4c # Reroll
            # 5 # Handle sweep and zilch
            

    def set_aside(self, dice):
        response = dice
        possible = ()
        current_roll = Counter(self.current_dice_roll)
        while True:
            if response.lower() == 'quit':
                return 'quit'
            if response.isnumeric():
                if len(response) <= len(self.current_dice_roll):
                    possible = ()
                    for num in response:
                        if num in current_roll and current_roll[num] > 0:
                            possible += (num,)
                            current_roll[num] -= 1
                if calculate_score(possible) > 0:
                    self.current_aside_pool += possible
                    for i in range(len(self.current_dice_roll)):
                        
                else:
                    response = self._input('That is not a valid response. Please select valid numbers.')
            else:
                response = self._input('Please enter numeric values.')
 
    def bank_dice(self):
        self.total_score += self.round_score
        self.round_score = 0

    def do_reroll(self):
        return roll_dice(len(self.current_dice_roll))

# if __name__ == "__main__":
#     game = GameOfGreed()
#     game.play()
a = '111'
c = tuple(int(_) for _ in a)
b = calculate_score(c)    
print(b)