from game_of_greed import GameOfGreed

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
def test_zilch():
    game = GameOfGreed()
    assert game.calculate_score((2,2,3,6,6,4)) == 0
# test_ones • rolls with various number of 1s should return correct score

# test_twos • rolls with various number of 2s should return correct score

# test_threes • rolls with various number of 3s should return correct score

# test_fours • rolls with various number of 4s should return correct score

# test_fives • rolls with various number of 5s should return correct score

# test_sixes • rolls with various number of 6s should return correct score

# test_straight • 1,2,3,4,5,6 should return correct score

# test_three_pairs • 3 pairs should return correct score

# test_two_trios • 2 sets of 3 should return correct score

# test_leftover_ones • 1s not used in set of 3 (or greater) should return correct score

# test_leftover_fives • 5s not used in set of 3 (or greater) should return correct score
