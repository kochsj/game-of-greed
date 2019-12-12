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
