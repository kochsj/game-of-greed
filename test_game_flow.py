import pytest
from game_of_greed import GameOfGreed
   

############################################################################
########################## Testing - Game Flow #############################
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
# def test_one_round():
#     flow = {
#         'prints' : [
#             'Welcome to Game of Greed',
#             'Rolling 6 dice',
#             'You rolled [1, 2, 2, 3, 3, 4]',
#             'You can bank 100 points or try for more',
#             'You have 5 dice remaining',
#             'Rolling 5 dice',
#             'You rolled [1, 2, 2, 3, 3]',
#             'You can bank 200 points or try for more',
#             'You have 4 dice remaining',
#             'Rolling 4 dice',
#             'You rolled [1, 2, 2, 3]',
#             'You can bank 300 points or try for more',
#             'You have 3 dice remaining',
#             'Rolling 3 dice',
#             'You rolled [1, 2, 2]',
#             'You can bank 400 points or try for more',
#             'You have 2 dice remaining',
#             'Rolling 2 dice',
#             'You rolled [1, 2]',
#             'You can bank 500 points or try for more',
#             'You have 1 dice remaining',
#             'You banked 500 points in round 1',
#             'You have 500 points total',
#             'Thanks for playing!'
#         ],
#         'prompts' : [
#             'Wanna play? ',
#             'Enter dice to keep: ',
#             'Roll again? ',
#             'Enter dice to keep: ',
#             'Roll again? ',
#             'Enter dice to keep: ',
#             'Roll again? ',
#             'Enter dice to keep: ',
#             'Roll again? ',
#             'Enter dice to keep: ',
#             'Roll again? ',
#         ],
#         'responses' : [
#             'y','1','y','1','y','1','y','1','y','1','n'
#         ],
#         'rolls' : [
#             [1, 2, 2, 3, 3, 4],
#             [1, 2, 2, 3, 3],
#             [1, 2, 2, 3],
#             [1, 2, 2],
#             [1, 2],
#         ]
#     }

#     mp = MockPlayer(**flow)

#     game = Game(mp.mock_print, mp.mock_input)

#     game._do_roll = mp.mock_roll

#     game.play(1)

#     assert mp.mop_up()

# def test_flow_scenario_1():

#     flow = {
#         'prints' : [
#             'Welcome to Game of Greed',
#             'Rolling 6 dice',
#             'You rolled [1, 2, 3, 4, 1, 2]',
#             'You can bank 100 points or try for more',
#             'You have 5 dice remaining',
#             'Rolling 5 dice',
#             'You rolled [3, 3, 3, 4, 1]',
#             'You can bank 500 points or try for more',
#             'You have 1 dice remaining',
#             'You banked 500 points in round 1',
#             'You have 500 points total',
#             'Thanks for playing!'
#         ],

#         'prompts' : [
#             'Wanna play? ',
#             'Enter dice to keep: ',
#             'Roll again? '
#         ],

#         'responses' : ['y','1','y','3331','n'],

#         'rolls' : [[1,2,3,4,1,2],[3,3,3,4,1]],
#     }

#     mp = MockPlayer(**flow)

#     game = Game(mp.mock_print, mp.mock_input)

#     game._do_roll = mp.mock_roll

#     game.play(1)

#     assert mp.mop_up()

# def test_flow_scenario_2():

#     flow = {
#         'prints' : [
#             'Welcome to Game of Greed',
#             'Rolling 6 dice',
#             'You rolled [1, 1, 1, 1, 5, 2]',
#             'You can bank 2050 points or try for more',
#             'You have 1 dice remaining',
#             'You banked 2050 points in round 1',
#             'You have 2050 points total',
#             'Thanks for playing!',
#         ],

#         'prompts' : [
#             'Wanna play? ',
#             'Enter dice to keep: ',
#             'Roll again? '
#         ],

#         'responses' : ['y','11115','n'],

#         'rolls' : [[1,1,1,1,5,2],],
#     }

#     mp = MockPlayer(**flow)

#     game = Game(mp.mock_print, mp.mock_input)

#     game._do_roll = mp.mock_roll

#     game.play(1)

#     assert mp.mop_up()

# def test_flow_zilch():

#     flow = {
#         'prints' : [
#             'Rolling 6 dice',
#             'You rolled [2, 2, 3, 4, 6, 6]',
#             'Oh noes! Zilch',
#         ],
#         'rolls' : [[2,2,3,4,6,6]],
#     }

#     mp = MockPlayer(**flow)

#     game = Game(mp.mock_print, mp.mock_input)

#     game._do_roll = mp.mock_roll

#     # Easier to test with hitting _do_round directly,
#     # no prob, but notice that protected method use is risky
#     game._do_round()

#     assert mp.mop_up()


###############################################
#####  Day 3 - Coming Soon               ######
###############################################
def test_validate_selected_dice():
    """"
    add a test to confirm that user's selected
    "keeper" dice are a valid subset of the user's roll
    """
    pass

def test_zilch_ends_round():
    """"
    add a test to confirm that a zilch roll
    ends the turn and no points are awarded
    """
    pass




###############################################
#####  Helper Class for Testing          ######
###############################################
class MockPlayer:
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


