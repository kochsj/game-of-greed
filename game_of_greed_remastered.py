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
        self._do_roll = roll_dice

    def play(self, num_rounds=10):
        """
        Greets user by printing ‘Welcome to Game of Greed’
        Prompts user with ‘Wanna play?’
        Handles the flow of the game
        """
        self.total_score = 0
        self._print('Welcome to Game of Greed')
        response = self._input('Wanna play? ')
        if response == 'y':
            rounds = 1
            # while self.total_score < 10_000 and rounds <= (num_rounds):
            while rounds <= (num_rounds):
                # self._print(f'Starting Round: {rounds}')
                round_score = self._turn()
                if round_score == 'quit': break
                self.total_score += round_score
                self._print(f'You banked {round_score} points in round {rounds}')
                rounds += 1
            # self._print(f'Rounds: {rounds} Final score: {self.total_score}')
            self._print(f'You have {self.total_score} points total')
            self._print(f'Thanks for playing!')
            return (self.total_score, rounds-1)
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
            self._print(f'Rolling {6 - len(dice_aside)} dice')
            current_dice_roll = self._do_roll(6 - (len(dice_aside) % 6))
            roll_score = self.calculate_score(current_dice_roll)

            # Print the roll ###################################################################
            # print_dice(current_dice_roll)
            self._print(f'You rolled {current_dice_roll}')
            # self._print(f'Round Score: {turn_score}')
            # self._print(f'Saved Dice: {dice_aside}')

            # Check for zilch ##################################################################
            if roll_score == 0:
                self._print('Oh noes! Zilch')
                return roll_score
            
            # Ask player to set aside ##########################################################
            player_prompts = self._save_dice(current_dice_roll)
            if player_prompts == 'quit':
                return 'quit'
            dice_aside += player_prompts[0]
            turn_score += player_prompts[1]

            # let player know where they stand, ask if they want to roll again #################
            if len(dice_aside) == 6:
                self._print(f'SWEEP!! You scored with all six dice! Rolling six again!')
                dice_aside = ''
                continue
            else:    
                # self._print(f'You entered: {response}')
                self._print(f'You can bank {turn_score} points or try for more')
                self._print(f'You have {6 - len(dice_aside)} dice remaining')
                response = self._input(f'Roll again? ')
            while response != 'y':
                if response.lower() == 'quit':
                    return 'quit'
                if response == 'n':
                    return turn_score
                response = self._input(f'Roll again? ')
                   

    def _save_dice(self, current_dice_roll):
        temp, turn_score = '', 0
        invalid_response = True

        while invalid_response:
            response = self._input('Enter dice to keep: ')

            if response.lower() == 'quit':
                return 'quit'

            # check that the player's response is in the current roll ##########################
            if response.isnumeric():
                valid = True
                mutable_roll = collections.Counter(current_dice_roll)
                for char in response:
                    if int(char) in mutable_roll and mutable_roll[int(char)] > 0:
                        temp += char
                        mutable_roll[int(char)] -=1
                    else:
                        self._print(f'{response} is an invalid response...')
                        valid = False
                        mutable_roll, temp = collections.Counter(current_dice_roll), ''
                        break
                # check that the player's response is scoring ##########################
                if valid and self.calculate_score(temp) > 0:
                    turn_score = self.calculate_score(temp)    
                    invalid_response = False
                    return [temp, turn_score]
                if valid and self.calculate_score(temp) == 0:
                    self._print(f'{response} is an invalid response...')
                    mutable_roll, temp = collections.Counter(current_dice_roll), ''
            else:
                self._print(f'{response} is an invalid response...')                  
                

    def calculate_score(self, current_dice_roll=(2,2,4,4,6,6)):
        """
        Accepts a dice roll as a parameter.
        Returns the calculated score.
        """

        # Cleaning input data for use
        if isinstance(current_dice_roll, str):
            formatted_dice_roll = (int(num) for num in current_dice_roll)    
            distribution_of_dice = collections.Counter(formatted_dice_roll)
        else:
            distribution_of_dice = collections.Counter(current_dice_roll)

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

class PlayerBot:
    """A bot that can play the game in the place of a player"""
    def __init__(self):
        self._current_roll = None
        self.dice_count = 6
        self._bank = ''

    def _print(self, *args):
        """
        PlayerBot replacement for Game._print
        "Reads" the current roll and saved score
        """
        print(args[0])

        if 'You rolled ' in args[0]:
            self._current_roll = [int(char) for char in args[0] if char.isnumeric()]

        if 'You can bank ' in args[0]:
            self._bank = ''
            a = [char for char in args[0] if char.isnumeric()]
            for num in a:
                self._bank += num
        
        if 'dice remaining' in args[0]:
            a = [char for char in args[0] if char.isnumeric()]
            self.dice_count = int(a[0])



    def _input(self, *args):
        """
        PlayerBot resonses for: 'Wanna play? ', 'Enter dice to keep: ', 'Roll again? ',
        """
        if args[0] == 'Wanna play? ':
            return 'y'

        if args[0] == 'Enter dice to keep: ':
            return self._select_dice(self._current_roll)

        if args[0] == 'Roll again? ':
            return self._roll_again()    
    


    def _select_dice(self, dice_roll):
        """
        Bot logic for selecting the best dice.
        """
        self.dice_count = len(dice_roll)

        distribution_of_dice = collections.Counter(dice_roll)

        for num in (2,3,4,6,5,1):
            a = '{}{}'.format(num, distribution_of_dice[num])

            if len(dice_roll) == 6 and set(distribution_of_dice.values()) == {2}: #three pairs
                selection = ''
                for num in dice_roll:
                    selection += str(num)
                return selection

            if len(distribution_of_dice) == 6: #straight • six/six unique numbers
                selection = ''
                for num in dice_roll:
                    selection += str(num)
                return selection

            if len(distribution_of_dice.values()) == 2 and set(distribution_of_dice.values()) == {3}: # two triples
                selection = ''
                for num in dice_roll:
                    selection += str(num)
                return selection

            # elif a[0] == '1' and a[1] >= '3':
            #     selection = ''
            #     for _ in range(int(a[1])):
            #         selection += '1'


            elif a[1] >= '3' and a[0] != '2' and a[0] != '3': # 3 or more of a kind, not 2s or 3s. also, check for ones
                selection = ''
                for _ in range(int(a[1])):
                    selection += a[0]
                if distribution_of_dice[1] > 0 and a[0] != '1':
                    for _ in range(distribution_of_dice[1]):
                        selection += '1'    
                return selection

            elif a[0] == '1' and a[1] > '0': # ones (one or two at this point)
                selection = ''
                for _ in range(int(a[1])):
                    selection += a[0]
                return selection

            elif a[0] == '5' and a[1] > '0': # fives (last resort, take all the fives)
                selection = ''
                if 1 not in dice_roll:
                    for _ in range(int(a[1])):
                        selection += a[0]
                    return selection
                continue

            elif a[1] >= '3' and a[0] == '2' or a[1] >= '3' and a[0] == '3': #check for twos and threes
                selection = ''
                for _ in range(int(a[1])):
                    selection += a[0]
                return selection

            
        

    def _roll_again(self):
        """
        Bot logic for deciding if it is a good idea to roll again.
        """
        # if self.dice_count > 3:
        #     return 'y'

        if self.dice_count >= 3 and int(self._bank) < 1000:
            return 'y'

        else:
            return 'n'    




if __name__ == "__main__":
    bot = PlayerBot()

    game = Game(bot._print, bot._input)
    games = 1000

    high_score = 0
    low_score = 10000
    total_score = 0

    shortest_game = 20

    for _ in range(games):
        game_score = game.play()

        total_score += game_score[0]
        shortest_game = game_score[1] if game_score[1] < shortest_game else shortest_game
        high_score = game_score[0] if game_score[0] > high_score else high_score
        low_score = game_score[0] if game_score[0] < low_score else low_score

    print('')
    print('')
    print('')
    # print('Shortest Game: ' + str(shortest_game))
    print('Average Round Score: ' + str(total_score/games//20))
    print('Average Game Score: ' + str(total_score/games))
    print('Highest Game Score: ' + str(high_score))
    print('Lowest Game Score:  ' + str(low_score))
    print('')
    print('')
    print('')