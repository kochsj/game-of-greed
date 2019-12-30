#############################################################################################
# CREDIT -> https://stackoverflow.com/questions/43560588/print-multiline-strings-side-by-side
#############################################################################################
dice_art = ["""""","""
 _______ 
|       |
|   •   |
|       |
 ¯¯¯¯¯¯¯ ""","""
 _______ 
|    •  |
|       |
|  •    |
 ¯¯¯¯¯¯¯ ""","""
 _______ 
|     • |
|   •   |
| •     |
 ¯¯¯¯¯¯¯ ""","""
 _______ 
| •   • |
|       |
| •   • |
 ¯¯¯¯¯¯¯ ""","""
 _______ 
| •   • |
|   •   |
| •   • |
 ¯¯¯¯¯¯¯ ""","""
 _______ 
| •   • |
| •   • |
| •   • |
 ¯¯¯¯¯¯¯ """,

]

def print_dice(current_roll=None):
    # player = [5, 1, 5, 3, 4, 5]
    # player = [0, 0, 0, 0, 0, 0]
    player = current_roll
    lines = [dice_art[i].splitlines() for i in player]
    for l in zip(*lines):
        print(*l, sep='')

# print_dice((3, 1, 2))

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

#####################################################################
# OLD METHOD ########################################################
#####################################################################
# def print_one(current_roll=None):
#     print(' _______')
#     print('|       |')
#     print('|   •   |')
#     print('|       |')
#     print(' ¯¯¯¯¯¯¯ ')

# def print_two(current_roll=None):
#     print(' _______')
#     print('|     • |')
#     print('|       |')
#     print('|  •    |')
#     print(' ¯¯¯¯¯¯¯ ')

# def print_three(current_roll=None):
#     print(' _______')
#     print('|     • |')
#     print('|   •   |')
#     print('| •     |')
#     print(' ¯¯¯¯¯¯¯ ')

# def print_four(current_roll=None):
#     print(' _______')
#     print('| •   • |')
#     print('|       |')
#     print('| •   • |')
#     print(' ¯¯¯¯¯¯¯ ')

# def print_five(current_roll=None):
#     print(' _______')
#     print('| •   • |')
#     print('|   •   |')
#     print('| •   • |')
#     print(' ¯¯¯¯¯¯¯ ')

# def print_six(current_roll=None):
#     print(' _______ ')
#     print('| •   • |')
#     print('| •   • |')
#     print('| •   • |')
#     print(' ¯¯¯¯¯¯¯ ')
