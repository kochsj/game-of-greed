import pytest
from game_of_greed import GameOfGreed

@pytest.fixture()
def game():
    return GameOfGreed()
# Testing - Game Flow
# 
# When calling play method ensure…
# proper greeting is displayed
def test_greeting():
    prints = ['Welcome to Game of Greed', 'Wanna play?', 'OK. Maybe another time', 'Great! Check back tomorrow :D']

    def print_for_testing(message):
        assert message == prints.pop(0)
    game = GameOfGreed(print_for_testing, print_for_testing)
    game.play()

# proper prompt is then shown
def test_prompt_is_shown():
    prints = ['Welcome to Game of Greed', 'Wanna play?', 'OK. Maybe another time', 'Great! Check back tomorrow :D']

    def print_for_testing(message):
        assert message == prints.pop(0)
    game = GameOfGreed(print_for_testing, print_for_testing)
    game.play()

# proper display based on user input of ‘y’ or anything else
def test_response_yes():
    prints = ['Welcome to Game of Greed', 'Wanna play?', 'Great! Check back tomorrow :D', 'OK. Maybe another time']
    def print_for_testing(message):
        assert message == prints.pop(0)
    game = GameOfGreed(print_for_testing, print_for_testing)
    game.play('y') # testing yes



# Testing - Calculate Score
# test_zilch • non scoring roll should return 0
def test_zilch(game):
    assert game.calculate_score((2,2,3,6,6,4)) == 0
# test_ones • rolls with various number of 1s should return correct score
def test_one_ones(game):
    assert game.calculate_score((2,2,3,1,6,4)) == 100
def test_two_ones(game):
    assert game.calculate_score((1,2,3,1,6,4)) == 200
def test_many_ones(game):
    assert game.calculate_score((1,1,1,1,1,1)) == 4_000

# test_twos • rolls with various number of 2s should return correct score
def test_one_twos(game):
    assert game.calculate_score((2,3,3,4,6,4)) == 0
def test_three_twos(game):
    assert game.calculate_score((2,2,2,4,6,4)) == 200
def test_many_twos(game):
    assert game.calculate_score((2,2,2,2,2,2)) == 800

# test_threes • rolls with various number of 3s should return correct score
def test_one_threes(game):
    assert game.calculate_score((2,2,3,4,6,4)) == 0
def test_three_threes(game):
    assert game.calculate_score((3,3,3,2,6,4)) == 300
def test_many_threes(game):
    assert game.calculate_score((3,3,3,3,3,3)) == 1_200

# test_fours • rolls with various number of 4s should return correct score
def test_one_fours(game):
    assert game.calculate_score((2,2,3,1,6,4)) == 100
def test_three_fours(game):
    assert game.calculate_score((2,2,3,4,4,4)) == 400
def test_many_fours(game):
    assert game.calculate_score((4,4,4,4,4,4)) == 1_600

# test_fives • rolls with various number of 5s should return correct score
def test_one_fives(game):
    assert game.calculate_score((2,2,3,5,6,4)) == 50
def test_three_fives(game):
    assert game.calculate_score((5,5,5,2,6,4)) == 500
def test_many_fives(game):
    assert game.calculate_score((5,5,5,5,5,5)) == 2_000

# test_sixes • rolls with various number of 6s should return correct score
def test_one_sixes(game):
    assert game.calculate_score((2,2,3,3,6,4)) == 0
def test_three_sixes(game):
    assert game.calculate_score((6,2,3,6,6,4)) == 600
def test_many_sixes(game):
    assert game.calculate_score((6,6,6,6,6,6)) == 2_400

# test_straight • 1,2,3,4,5,6 should return correct score
def test_a_straight(game):
    assert game.calculate_score((1,2,3,4,5,6)) == 1_500
def test_a_mixed_up_straight(game):
    assert game.calculate_score((4,6,1,5,3,2)) == 1_500    
# test_three_pairs • 3 pairs should return correct score
def test_three_pairs(game):
    assert game.calculate_score((2,2,4,4,6,6)) == 1_500
# test_two_trios • 2 sets of 3 should return correct score
def test_two_trios(game):
    assert game.calculate_score((2,2,2,3,3,3)) == 500
def test_two_mixed_up_trios(game):
    assert game.calculate_score((4,6,4,6,4,6)) == 1000    
# test_leftover_ones • 1s not used in set of 3 (or greater) should return correct score
def test_one_leftover_ones(game):
    assert game.calculate_score((3,3,3,4,6,1)) == 400
def test_two_leftover_ones(game):
    assert game.calculate_score((6,1,4,6,1,6)) == 800
# test_leftover_fives • 5s not used in set of 3 (or greater) should return correct score
def test_one_leftover_fives(game):
    assert game.calculate_score((3,3,3,4,6,5)) == 350
def test_two_leftover_fives(game):
    assert game.calculate_score((6,5,4,6,5,6)) == 700

# Application should simulate rolling between 1 and 6 dice
def test_dice_roll_none(game):
    assert game.roll_dice(0) == ()
def test_dice_roll_one(game):
    assert game.roll_dice(1) == (1) or (2) or (3) or (4) or (5) or (6)
def test_dice_roll_two(game):
    assert len(game.roll_dice(2)) == 2