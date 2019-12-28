import pytest
from game_of_greed_remastered import Game, roll_dice

@pytest.fixture()
def game():
    return Game()

@pytest.mark.parametrize("dice,expected",[
    ((1,), 100),
    ((2,), 0),
    ((3,), 0),
    ((4,), 0),
    ((5,), 50),
    ((6,), 0),
    ((1,1), 200),
    ((2,2), 0),
    ((3,3), 0),
    ((4,4), 0),
    ((5,5), 100),
    ((6,6), 0),
    ((1,1,1,), 1000),
    ((2,2,2,), 200),
    ((3,3,3,), 300),
    ((4,4,4,), 400),
    ((5,5,5,), 500),
    ((6,6,6,), 600),
    ((1,1,1,1), 2000),
    ((2,2,2,2), 400),
    ((3,3,3,3), 600),
    ((4,4,4,4), 800),
    ((5,5,5,5), 1000),
    ((6,6,6,6), 1200),
    ((1,1,1,1,1), 3000),
    ((2,2,2,2,2), 600),
    ((3,3,3,3,3), 900),
    ((4,4,4,4,4), 1200),
    ((5,5,5,5,5), 1500),
    ((6,6,6,6,6), 1800),
    ((1,1,1,1,1,1), 4000),
    ((2,2,2,2,2,2), 800),
    ((3,3,3,3,3,3), 1200),
    ((4,4,4,4,4,4), 1600),
    ((5,5,5,5,5,5), 2000),
    ((6,6,6,6,6,6), 2400),
])
def test_calculate_score(game, dice, expected):
    actual = game.calculate_score(dice)
    assert actual == expected

def test_calc_score_simple():
    game = Game()
    actual = game.calculate_score((1,2))
    expected = 100
    assert expected == actual

@pytest.mark.parametrize("keepers,expected",[
    ((6,6,6,1), 700),
    ((6,6,6,1,1,3), 800),
    ((1,2,3,4,5,6), 1500),
    ((1,2,4,5,3,6), 1500),
    ((1,1,2,2,5,5), 1500),
    ((2,2,2,3,3,3), 500),
    ((1,1,1,5,5,5), 1500),
])
def test_calculate_score_fancy(game, keepers, expected):
    actual = game.calculate_score(keepers)
    assert actual == expected


def test_zilch(game):
    expected = 0
    actual = game.calculate_score((2,3,4,6,2,3))
    assert actual == expected


def test_three_pairs(game):
    expected = 0
    actual = game.calculate_score((2,2,3,3,4))
    assert expected == actual

def test_three_pairs_with_ones(game):
    expected = 200
    actual = game.calculate_score((1,1,2,2,3))
    assert expected == actual

def test_module_doc():
    assert Game.__doc__ != None

@pytest.mark.parametrize("num_dice",[1,2,3,4,5,6])
def test_roll(num_dice):
    game = Game()
    roll = roll_dice(num_dice)
    assert len(roll) == num_dice
    for val in roll:
        assert 1 <= val <= 6

# ###############################################
# #####  Day 1                             ######
# ###############################################

def test_flow_no():

    flow = {
        'prints' : ['Welcome to Game of Greed','OK. Maybe later'],
        'prompts' : ['Wanna play? '],
        'responses' : ['no'],
    }

    mp = MockPlayer(**flow)

    game = Game(mp.mock_print, mp.mock_input)

    game.do_roll = mp.mock_roll

    game.play()

    assert mp.mop_up()

###############################################
#####  Day 2                             ######
###############################################
def test_one_round():
    flow = {
        'prints' : [
            'Welcome to Game of Greed',
            'Rolling 6 dice',
            'You rolled [1, 2, 2, 3, 3, 4]',
            'You can bank 100 points or try for more',
            'You have 5 dice remaining',
            'Rolling 5 dice',
            'You rolled [1, 2, 2, 3, 3]',
            'You can bank 200 points or try for more',
            'You have 4 dice remaining',
            'Rolling 4 dice',
            'You rolled [1, 2, 2, 3]',
            'You can bank 300 points or try for more',
            'You have 3 dice remaining',
            'Rolling 3 dice',
            'You rolled [1, 2, 2]',
            'You can bank 400 points or try for more',
            'You have 2 dice remaining',
            'Rolling 2 dice',
            'You rolled [1, 2]',
            'You can bank 500 points or try for more',
            'You have 1 dice remaining',
            'You banked 500 points in round 1',
            'You have 500 points total',
            'Thanks for playing!'
        ],
        'prompts' : [
            'Wanna play? ',
            'Enter dice to keep: ',
            'Roll again? ',
            'Enter dice to keep: ',
            'Roll again? ',
            'Enter dice to keep: ',
            'Roll again? ',
            'Enter dice to keep: ',
            'Roll again? ',
            'Enter dice to keep: ',
            'Roll again? ',
        ],
        'responses' : [
            'y','1','y','1','y','1','y','1','y','1','n'
        ],
        'rolls' : [
            [1, 2, 2, 3, 3, 4],
            [1, 2, 2, 3, 3],
            [1, 2, 2, 3],
            [1, 2, 2],
            [1, 2],
        ]
    }

    mp = MockPlayer(**flow)

    game = Game(mp.mock_print, mp.mock_input)

    game._do_roll = mp.mock_roll

    game.play(1)

    assert mp.mop_up()

def test_flow_scenario_1():

    flow = {
        'prints' : [
            'Welcome to Game of Greed',
            'Rolling 6 dice',
            'You rolled [1, 2, 3, 4, 1, 2]',
            'You can bank 100 points or try for more',
            'You have 5 dice remaining',
            'Rolling 5 dice',
            'You rolled [3, 3, 3, 4, 1]',
            'You can bank 500 points or try for more',
            'You have 1 dice remaining',
            'You banked 500 points in round 1',
            'You have 500 points total',
            'Thanks for playing!'
        ],

        'prompts' : [
            'Wanna play? ',
            'Enter dice to keep: ',
            'Roll again? '
        ],

        'responses' : ['y','1','y','3331','n'],

        'rolls' : [[1,2,3,4,1,2],[3,3,3,4,1]],
    }

    mp = MockPlayer(**flow)

    game = Game(mp.mock_print, mp.mock_input)

    game._do_roll = mp.mock_roll

    game.play(1)

    assert mp.mop_up()

def test_flow_scenario_2():

    flow = {
        'prints' : [
            'Welcome to Game of Greed',
            'Rolling 6 dice',
            'You rolled [1, 1, 1, 1, 5, 2]',
            'You can bank 2050 points or try for more',
            'You have 1 dice remaining',
            'You banked 2050 points in round 1',
            'You have 2050 points total',
            'Thanks for playing!',
        ],

        'prompts' : [
            'Wanna play? ',
            'Enter dice to keep: ',
            'Roll again? '
        ],

        'responses' : ['y','11115','n'],

        'rolls' : [[1,1,1,1,5,2],],
    }

    mp = MockPlayer(**flow)

    game = Game(mp.mock_print, mp.mock_input)

    game._do_roll = mp.mock_roll

    game.play(1)

    assert mp.mop_up()

def test_flow_zilch():

    flow = {
        'prints' : [
            'Rolling 6 dice',
            'You rolled [2, 2, 3, 4, 6, 6]',
            'Oh noes! Zilch',
        ],
        'rolls' : [[2,2,3,4,6,6]],
    }

    mp = MockPlayer(**flow)

    game = Game(mp.mock_print, mp.mock_input)

    game._do_roll = mp.mock_roll

    # Easier to test with hitting _do_round directly,
    # no prob, but notice that protected method use is risky
    game._turn()

    assert mp.mop_up()


# ###############################################
# #####  Day 3 - Coming Soon               ######
# ###############################################
# def test_validate_selected_dice():
#     """"
#     add a test to confirm that user's selected
#     "keeper" dice are a valid subset of the user's roll
#     """
#     pass

# def test_zilch_ends_round():
#     """"
#     add a test to confirm that a zilch roll
#     ends the turn and no points are awarded
#     """
#     pass




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

# @pytest.fixture()
# def game():
#     return Game()

# @pytest.mark.parametrize("roll, keepers, expected",[
#     ([1,2,3],(1,),True),
#     ([1,2,3],(1,2),True),
#     ([1,2,3],(1,2,3),True),
#     ([1,2,3],(6,),False),
#     ([1,2,3],(1,1),False),
# ])
# def test_validate(game, roll, keepers, expected):
#     actual = game.validate(roll, keepers)
#     assert actual == expected

# @pytest.mark.parametrize("roll,expected_keepers",[([1,2,3],(1,)),([4,5,6],(5,))])
# def test_def_validate_roll_success(roll, expected_keepers):

#     def my_print(msg, *args):
#         assert msg == roll

#     def my_input(msg, *args):
#         assert msg == 'Enter dice to keep: '
#         keeper_string = ''
#         for val in expected_keepers:
#             keeper_string += str(val)

#         return keeper_string

#     game = Game(my_print, my_input)

#     keepers = game.validate_roll(roll)

#     assert keepers == expected_keepers

# @pytest.mark.parametrize("roll,expected_keepers",[
#     ([1,2,3],(1,)),
#     ([4,5,6],(5,)),
# ])
# def test_def_validate_roll_fail(roll, expected_keepers):

#     prints = ['No way pal', roll, 'No way pal',roll]

#     inputs = ['0','0', str(expected_keepers[0])]

#     def my_print(msg, *args):
#         assert msg == prints.pop(0)

#     def my_input(msg, *args):
#         assert msg == 'Enter dice to keep: '
#         return inputs.pop(0)

#     game = Game(my_print, my_input)

#     keepers = game.validate_roll(roll)

#     assert keepers == expected_keepers


# @pytest.mark.parametrize("roll,expected_keepers",[
#     ((1,2,3),(1,)),
#     ((4,5,6),(5,)),
#     ((1,2,1,4,1),(1,1,1)),

# ])
# def test_strip_superflous(roll, expected_keepers):
#     game = Game()
#     actual = game._strip_superflous(roll)
#     assert actual == expected_keepers

# def test_straight():
#     game = Game()
#     actual = game.calculate_score((3,2,4,5,1,6))
#     expected = 1500
#     assert actual == expected

# def test_3_pairs():
#     game = Game()
#     actual = game.calculate_score((3,2,4,3,2,4))
#     expected = 1500
#     assert actual == expected


############################################################################
####################### Testing - Calculate Score ##########################
############################################################################
# test_zilch • non scoring roll should return 0
############################################################################
def test_zilch(game):
    assert game.calculate_score((2,2,3,6,6,4)) == 0

############################################################################
# test_ones • rolls with various number of 1s should return correct score
############################################################################
def test_one_ones(game):
    assert game.calculate_score((1,)) == 100
    assert game.calculate_score((2,2,3,1,6,4)) == 100
def test_three_ones(game):
    assert game.calculate_score((1,1,1)) == 1000
    assert game.calculate_score((1,2,1,1,6,4)) == 1000
def test_many_ones(game):
    assert game.calculate_score((1,1,1,1,1,1)) == 4_000

############################################################################
# test_twos • rolls with various number of 2s should return correct score
############################################################################
def test_one_twos(game):
    assert game.calculate_score((2,)) == 0
    assert game.calculate_score((2,3,3,4,6,4)) == 0
def test_three_twos(game):
    assert game.calculate_score((2,2,2)) == 200
    assert game.calculate_score((2,2,2,4,6,4)) == 200
def test_many_twos(game):
    assert game.calculate_score((2,2,2,2,2,2)) == 800

############################################################################
# test_threes • rolls with various number of 3s should return correct score
############################################################################
def test_one_threes(game):
    assert game.calculate_score((3,)) == 0
    assert game.calculate_score((2,2,3,4,6,4)) == 0
def test_three_threes(game):
    assert game.calculate_score((3,3,3)) == 300
    assert game.calculate_score((3,3,3,2,6,4)) == 300
def test_many_threes(game):
    assert game.calculate_score((3,3,3,3,3,3)) == 1_200

############################################################################
# test_fours • rolls with various number of 4s should return correct score
############################################################################
def test_one_fours(game):
    assert game.calculate_score((4,)) == 0
    assert game.calculate_score((2,2,3,1,6,4)) == 100
def test_three_fours(game):
    assert game.calculate_score((4,4,4)) == 400
    assert game.calculate_score((2,2,3,4,4,4)) == 400
def test_many_fours(game):
    assert game.calculate_score((4,4,4,4,4,4)) == 1_600

############################################################################
# test_fives • rolls with various number of 5s should return correct score
############################################################################
def test_one_fives(game):
    assert game.calculate_score((5,)) == 50
    assert game.calculate_score((2,2,3,5,6,4)) == 50
def test_three_fives(game):
    assert game.calculate_score((5,5,5)) == 500
    assert game.calculate_score((5,5,5,2,6,4)) == 500
def test_many_fives(game):
    assert game.calculate_score((5,5,5,5,5,5)) == 2_000

############################################################################
# test_sixes • rolls with various number of 6s should return correct score
############################################################################
def test_one_sixes(game):
    assert game.calculate_score((6,)) == 0
    assert game.calculate_score((2,2,3,3,6,4)) == 0
def test_three_sixes(game):
    assert game.calculate_score((6,6,6)) == 600
    assert game.calculate_score((6,2,3,6,6,4)) == 600
def test_many_sixes(game):
    assert game.calculate_score((6,6,6,6,6,6)) == 2_400

############################################################################
# test_straight • 1,2,3,4,5,6 should return correct score
############################################################################
def test_a_straight(game):
    assert game.calculate_score((1,2,3,4,5,6)) == 1_500
def test_a_mixed_up_straight(game):
    assert game.calculate_score((4,6,1,5,3,2)) == 1_500

############################################################################    
# test_three_pairs • 3 pairs should return correct score
############################################################################
def test_three_pairs(game):
    assert game.calculate_score((2,2,4,4,6,6)) == 1_500

############################################################################    
# test_two_trios • 2 trios should return correct score
############################################################################    
def test_two_trios(game):
    assert game.calculate_score((1,1,1,5,5,5)) == 1_500

def test_two_trios_twos_and_threes(game):
    assert game.calculate_score((2,2,2,3,3,3)) == 500

############################################################################
# test_two_trios • 2 sets of 3 should return correct score
############################################################################
def test_two_trios(game):
    assert game.calculate_score((2,2,2,3,3,3)) == 500
def test_two_mixed_up_trios(game):
    assert game.calculate_score((4,6,4,6,4,6)) == 1000 

############################################################################ 
# test_leftover_ones • 1s not used in set of 3 (or greater) should return correct score
############################################################################
def test_one_leftover_ones(game):
    assert game.calculate_score((3,3,3,4,6,1)) == 400
def test_two_leftover_ones(game):
    assert game.calculate_score((6,1,4,6,1,6)) == 800

############################################################################
# test_leftover_fives • 5s not used in set of 3 (or greater) should return correct score
############################################################################
def test_one_leftover_fives(game):
    assert game.calculate_score((3,3,3,4,6,5)) == 350
def test_two_leftover_fives(game):
    assert game.calculate_score((6,5,4,6,5,6)) == 700

############################################################################
# Application should simulate rolling between 1 and 6 dice
############################################################################
def test_dice_roll_none(game):
    assert roll_dice(0) == ()
def test_dice_roll_one(game):
    assert roll_dice(1) == (1) or (2) or (3) or (4) or (5) or (6)
def test_dice_roll_two(game):
    assert len(roll_dice(2)) == 2
def test_dice_roll_many(game):
    assert len(roll_dice(6)) == 6