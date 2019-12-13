import pytest
import collections
from game_of_greed import GameOfGreed
   

############################################################################
########################## Testing - Game Flow #############################

        # OLD TESTS
############################################################################
# When calling play method, ensure proper greeting is displayed
############################################################################
# def test_greeting():
#     prints = ['Wanna play? (y or n):  ', 'OK. Maybe another time', 'Great! Check back tomorrow :D']

#     def print_for_testing(message):
#         assert message == prints.pop(0)
#     game = GameOfGreed(print_for_testing, print_for_testing)
#     game.play()

############################################################################
# proper prompt is then shown
############################################################################
# def test_prompt_is_shown():
#     prints = ['Wanna play? (y or n):  ', 'OK. Maybe another time', 'Great! Check back tomorrow :D']

#     def print_for_testing(message):
#         assert message == prints.pop(0)
#     game = GameOfGreed(print_for_testing, print_for_testing)
#     game.play()

############################################################################
# proper display based on user input of ‘n’ or anything else
############################################################################
# def test_response_no():
#     prints = ['Wanna play? (y or n):  ', 'OK. Maybe another time', 'Great! Check back tomorrow :D']
#     def print_for_testing(message):
#         assert message == prints.pop(0)
#     game = GameOfGreed(print_for_testing, print_for_testing)
#     game.play('n') # testing no

############################################################################
# Application should allow user to set aside dice each roll
# ############################################################################
# def test_set_aside_one():
#     prints = ['What will you set aside? (5,)  ']
#     def print_for_testing(message):
#         assert message == prints.pop(0)
#     game = GameOfGreed(print_for_testing, print_for_testing)
#     game.set_aside((5,))
#     assert game.aside == (5,)
# def test_set_aside_two(game):
#     game.set_aside(5)
#     game.set_aside(5)
#     assert game.aside == (5,5)
# def test_set_aside_many(game):
#     game.set_aside(3)
#     game.set_aside(3)
#     game.set_aside(3)
#     game.set_aside(3)
#     assert game.aside == (3,3,3,3)    


def test_flow_no():

    flow = {
        'prints' : ['OK. Maybe another time'],
        'prompts' : ['Wanna play? (y or n):  '],
        'responses' : ['no'],
    }

    mp = MockPlayer(**flow)

    game = GameOfGreed(1, mp.mock_print, mp.mock_input)

    game.roll_dice = mp.mock_roll

    game.play()

    assert mp.mop_up()

###############################################
#####  Day 2                             ######
###############################################
def test_scenario_one():
    flow = {
        'prints' : [
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 1 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 0',
            '**************************************************************',
            '                                                              ',
            'Dice on table: (1, 2, 2, 3, 3, 4)',
            'Your current aside pool: ()',
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 1 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 0',
            '**************************************************************',
            '                                                              ',
            'Dice on table: (2, 2, 3, 3, 4)',
            'Your current aside pool: (1,)',
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 1 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 0',
            '**************************************************************',
            '                                                              ',
            'Dice on table: (5, 2, 2, 4, 5)',
            'Your current aside pool: (1,)',
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 1 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 0',
            '**************************************************************',
            '                                                              ',
            'Dice on table: (2, 2, 4)',
            'Your current aside pool: (1, 5, 5)',
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 1 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 0',
            '**************************************************************',
            '                                                              ',
            'Dice on table: (1, 1, 4)',
            'Your current aside pool: (1, 5, 5)',
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 1 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 0',
            '**************************************************************',
            '                                                              ',
            'Dice on table: (4,)',
            'Your current aside pool: (1, 5, 5, 1, 1)',
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 2 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 400',
            '**************************************************************',
            '                                                              ',
            'Dice on table: (5, 3, 1, 6, 6, 2)',
            'Your current aside pool: ()'
        ],
        'prompts' : [
            'Wanna play? (y or n):  ',
            'What will you set aside? Enter a to open up the aside pool.  ',
            'What will you set aside? (1, 2, 2, 3, 3, 4)  ',
            'How many?  ',
            'No scoring values... bank your points (currently: 100) "b"... or roll again..."r".  ',
            'Set your points aside "a"? Or bank what you have (currently: 100) "b"? Enter "r" to roll again.',
            'What will you set aside? (5, 2, 2, 4, 5)  ',
            'How many?  ',
            'No scoring values... bank your points (currently: 200) "b"... or roll again..."r".  ',
            'Set your points aside "a"? Or bank what you have (currently: 200) "b"? Enter "r" to roll again.',
            'What will you set aside? (1, 1, 4)  ',
            'How many?  ',
            'Please enter a number between 1 and 2...Select a number to set aside again.  ', #add a test to confirm that user's selected "keeper" dice are a valid subset of the user's roll
            'How many?  ',
            'No scoring values... bank your points (currently: 400) "b"... or roll again..."r".  ',
            'What will you set aside? Enter a to open up the aside pool.  '
        ],
        'responses' : [
            'y', 'a', '1', '1', 'r', 'a', '5', '2', 'r', 'a', '1', '3', '1', '2', 'b', 'quit'
        ],
        'rolls' : [
            (1, 2, 2, 3, 3, 4),
            (5, 2, 2, 4, 5),
            (1, 1, 4),
            (5, 3, 1, 6, 6, 2)
        ]
    }

    mp = MockPlayer(**flow)

    game = GameOfGreed(1, mp.mock_print, mp.mock_input, mp.mock_roll)

    game.play()

    assert mp.mop_up()

def test_flow_zilch_ends_round():

    flow = {
        'prints' : [
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 1 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 0',
            '**************************************************************',
            '                                                              ',
            'Dice on table: (6, 6, 6, 6, 6, 6)',
            'Your current aside pool: ()',
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 1 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 0',
            '**************************************************************',
            '                                                              ',
            'Dice on table: ()',
            'Your current aside pool: (6, 6, 6, 6, 6, 6)',
            ' ',
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 1 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 0',
            '**************************************************************',
            '                                                              ',
            'Dice on table: (1, 2, 6, 6, 4, 3)',
            'Your current aside pool: (6, 6, 6, 6, 6, 6)',
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 1 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 0',
            '**************************************************************',
            '                                                              ',
            'Dice on table: (2, 6, 6, 4, 3)',
            'Your current aside pool: (6, 6, 6, 6, 6, 6, 1)',
            ' ',
            '                                                              ',
            '                                                              ',
            '**************************************************************',
            'Round 2 - - - - - - - - - - - - - - - - - - TOTAL SCORE: 0',
            '**************************************************************',
            '                                                              ',
            'Dice on table: (5, 5, 2, 1, 6, 6)',
            'Your current aside pool: ()'
        ],
        'prompts' : [
            'Wanna play? (y or n):  ',
            'What will you set aside? Enter a to open up the aside pool.  ',
            'What will you set aside? (6, 6, 6, 6, 6, 6)  ',
            'How many?  ',
            'SWEEP! You scored with all 6 dice! Rolling 6 new dice... You still have 2400 points set aside!',
            'Set your points aside "a"? Or bank what you have (currently: 2400) "b"? Enter "r" to roll again.',
            'What will you set aside? (1, 2, 6, 6, 4, 3)  ',
            'How many?  ',
            'No scoring values... bank your points (currently: 2500) "b"... or roll again..."r".  ',
            '(2, 3, 4, 6, 6) Zilch! You rolled no scoring values. You lost your 2500 points set aside. Round 1 over.', ######Zilch ends round######
            'What will you set aside? Enter a to open up the aside pool.  '
        ],
        'responses' : [
            'y', 'a', '6', '6', 'a', 'a', '1', '1', 'r', 'r', 'quit'
        ],
        'rolls' : [
            (6, 6, 6, 6, 6, 6),
            (1, 2, 6, 6, 4, 3),
            (2, 3, 4, 6, 6),
            (5, 5, 2, 1, 6, 6)
        ],
    }

    mp = MockPlayer(**flow)

    game = GameOfGreed(1, mp.mock_print, mp.mock_input, mp.mock_roll)

    game.play()

    assert mp.mop_up()

###############################################
#####  Helper Class for Testing          ######
###############################################
class MockPlayer:
    """
    Creates a mock player to represent a player 'playing' the game
    Used just for testing
    Redefines the print, input, and roll methods of the gameofgreed class
    """
    def __init__(self, prints=[], prompts=[], responses=[], rolls=[]):
        self.prints = prints
        self.prompts = prompts
        self.responses = responses
        self.rolls = rolls

    def mock_print(self, *args):
        if len(self.prints):
            current_print = self.prints.pop(0)
            assert args[0] == current_print

    def mock_input(self, *args):
        if len(self.prompts):
            current_prompt = self.prompts.pop(0)
            assert args[0] == current_prompt

        if len(self.responses):
            current_response = self.responses.pop(0)
            return current_response

    def mock_roll(self, num_dice):
        if len(self.rolls):
            current_roll = self.rolls.pop(0)
            return current_roll

    def mop_up(self):
        assert len(self.prints) == 0
        assert len(self.prompts) == 0
        assert len(self.responses) == 0
        assert len(self.rolls) == 0
        return True

###############################################
#####  Mock Player Class for Testing     ######
###############################################
class MockPlayer:

    def __init__(self):
        self.roll = None
        self.game = None
        self.roll_values = None
        self.dict_values = None
        self.selected_die = None

    def _print(self, *args):

        msg = args[0]

        if msg.startswith('You rolled'):
            self.roll = [int(char) for char in msg if char.isdigit()]

        print(msg)

    def _input(self, *args):
        prompt = args[0]

        if prompt == 'Wanna play? (y or n):  ':
            print(prompt,'y')
            return 'y'

        if prompt == 'What will you set aside? Enter a to open up the aside pool.  ':
            print(prompt, 'a')
            return 'a'

        if prompt.startswith('What will you set aside?'):
            self.roll_values = _clean_roll(prompt)
            self.dict_values = collections.Counter(self.roll_values)
            if '1' in self.dict_values:
                self.selected_die = '1'
                print(prompt, '1')
                return '1'
            if '5' in self.dict_values:
                self.selected_die = '5'
                print(prompt, '5')
                return '5'
            for key in self.dict_values:
                if key != '1' and key != '5' and self.dict_values[key] >= '3':
                    self.selected_die = key
                    print(prompt, key)
                    return str(key)    

        if prompt == 'How many?  ':
            all_of_them = self.dict_values[self.selected_die]
            self.dict_values[self.selected_die] = 0
            print(prompt, f'{all_of_them}')
            return str(all_of_them)

        if prompt.startswith('Set your points aside "a"'):

            print(prompt, 'b')
            return('b')


def _clean_roll(prompt):
    clean = prompt.split('(')
    cleaner = clean[1].split(')')
    roll_values_list = cleaner[0].split(', ')
    return tuple(roll_values_list)

if __name__ == "__main__":
    bot = MockPlayer()
    game = GameOfGreed(10, bot._print, bot._input)
    bot.game = game
    game.play()            