# import pytest
# from game_of_greed import Game, roll_dice

# @pytest.fixture()
# def game():
#     return Game()

# ############################################################################
# ####################### Testing - Calculate Score ##########################
# ############################################################################
# # test_zilch • non scoring roll should return 0
# ############################################################################
# def test_zilch(game):
#     assert game.calculate_score((2,2,3,6,6,4)) == 0

# ############################################################################
# # test_ones • rolls with various number of 1s should return correct score
# ############################################################################
# def test_one_ones(game):
#     assert game.calculate_score((1,)) == 100
#     assert game.calculate_score((2,2,3,1,6,4)) == 100
# def test_three_ones(game):
#     assert game.calculate_score((1,1,1)) == 1000
#     assert game.calculate_score((1,2,1,1,6,4)) == 1000
# def test_many_ones(game):
#     assert game.calculate_score((1,1,1,1,1,1)) == 4_000

# ############################################################################
# # test_twos • rolls with various number of 2s should return correct score
# ############################################################################
# def test_one_twos(game):
#     assert game.calculate_score((2,)) == 0
#     assert game.calculate_score((2,3,3,4,6,4)) == 0
# def test_three_twos(game):
#     assert game.calculate_score((2,2,2)) == 200
#     assert game.calculate_score((2,2,2,4,6,4)) == 200
# def test_many_twos(game):
#     assert game.calculate_score((2,2,2,2,2,2)) == 800

# ############################################################################
# # test_threes • rolls with various number of 3s should return correct score
# ############################################################################
# def test_one_threes(game):
#     assert game.calculate_score((3,)) == 0
#     assert game.calculate_score((2,2,3,4,6,4)) == 0
# def test_three_threes(game):
#     assert game.calculate_score((3,3,3)) == 300
#     assert game.calculate_score((3,3,3,2,6,4)) == 300
# def test_many_threes(game):
#     assert game.calculate_score((3,3,3,3,3,3)) == 1_200

# ############################################################################
# # test_fours • rolls with various number of 4s should return correct score
# ############################################################################
# def test_one_fours(game):
#     assert game.calculate_score((4,)) == 0
#     assert game.calculate_score((2,2,3,1,6,4)) == 100
# def test_three_fours(game):
#     assert game.calculate_score((4,4,4)) == 400
#     assert game.calculate_score((2,2,3,4,4,4)) == 400
# def test_many_fours(game):
#     assert game.calculate_score((4,4,4,4,4,4)) == 1_600

# ############################################################################
# # test_fives • rolls with various number of 5s should return correct score
# ############################################################################
# def test_one_fives(game):
#     assert game.calculate_score((5,)) == 50
#     assert game.calculate_score((2,2,3,5,6,4)) == 50
# def test_three_fives(game):
#     assert game.calculate_score((5,5,5)) == 500
#     assert game.calculate_score((5,5,5,2,6,4)) == 500
# def test_many_fives(game):
#     assert game.calculate_score((5,5,5,5,5,5)) == 2_000

# ############################################################################
# # test_sixes • rolls with various number of 6s should return correct score
# ############################################################################
# def test_one_sixes(game):
#     assert game.calculate_score((6,)) == 0
#     assert game.calculate_score((2,2,3,3,6,4)) == 0
# def test_three_sixes(game):
#     assert game.calculate_score((6,6,6)) == 600
#     assert game.calculate_score((6,2,3,6,6,4)) == 600
# def test_many_sixes(game):
#     assert game.calculate_score((6,6,6,6,6,6)) == 2_400

# ############################################################################
# # test_straight • 1,2,3,4,5,6 should return correct score
# ############################################################################
# def test_a_straight(game):
#     assert game.calculate_score((1,2,3,4,5,6)) == 1_500
# def test_a_mixed_up_straight(game):
#     assert game.calculate_score((4,6,1,5,3,2)) == 1_500

# ############################################################################    
# # test_three_pairs • 3 pairs should return correct score
# ############################################################################
# def test_three_pairs(game):
#     assert game.calculate_score((2,2,4,4,6,6)) == 1_500

# ############################################################################    
# # test_two_trios • 2 trios should return correct score
# ############################################################################    
# def test_two_trios(game):
#     assert game.calculate_score((1,1,1,5,5,5)) == 1_500

# def test_two_trios_twos_and_threes(game):
#     assert game.calculate_score((2,2,2,3,3,3)) == 500

# ############################################################################
# # test_two_trios • 2 sets of 3 should return correct score
# ############################################################################
# def test_two_trios(game):
#     assert game.calculate_score((2,2,2,3,3,3)) == 500
# def test_two_mixed_up_trios(game):
#     assert game.calculate_score((4,6,4,6,4,6)) == 1000 

# ############################################################################ 
# # test_leftover_ones • 1s not used in set of 3 (or greater) should return correct score
# ############################################################################
# def test_one_leftover_ones(game):
#     assert game.calculate_score((3,3,3,4,6,1)) == 400
# def test_two_leftover_ones(game):
#     assert game.calculate_score((6,1,4,6,1,6)) == 800

# ############################################################################
# # test_leftover_fives • 5s not used in set of 3 (or greater) should return correct score
# ############################################################################
# def test_one_leftover_fives(game):
#     assert game.calculate_score((3,3,3,4,6,5)) == 350
# def test_two_leftover_fives(game):
#     assert game.calculate_score((6,5,4,6,5,6)) == 700

# ############################################################################
# # Application should simulate rolling between 1 and 6 dice
# ############################################################################
# def test_dice_roll_none(game):
#     assert roll_dice(0) == ()
# def test_dice_roll_one(game):
#     assert roll_dice(1) == (1) or (2) or (3) or (4) or (5) or (6)
# def test_dice_roll_two(game):
#     assert len(roll_dice(2)) == 2
# def test_dice_roll_many(game):
#     assert len(roll_dice(6)) == 6

# ############################################################################
# # Application should allow “banking” current score
# ############################################################################
# def test_bank_one(game):
#     dice = game.calculate_score((5,))
#     game.bank_dice(dice)
#     assert game.total_score == 50
# def test_bank_triple(game):
#     dice = game.calculate_score((2,2,2))
#     game.bank_dice(dice)
#     assert game.total_score == 200
# def test_bank_many(game):
#     dice = game.calculate_score((1,1,1,1,1,1))
#     game.bank_dice(dice)
#     assert game.total_score == 4000    

