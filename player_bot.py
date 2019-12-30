import collections
from game_of_greed_remastered import Game

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

        if self.dice_count >= 3 and int(self._bank) < 1000:
            return 'y'

        else:
            return 'n'

if __name__ == "__main__":
    bot = PlayerBot()

    game = Game(bot._print, bot._input)
    games = 1000
    num_rounds = 20

    high_score = 0
    low_score = 10000
    total_score = 0
    total_rounds = 0

    shortest_game = 20

    for _ in range(games):
        game_score = game.play(num_rounds)

        total_score += game_score[0]
        total_rounds += game_score[1]
        shortest_game = game_score[1] if game_score[1] < shortest_game else shortest_game
        high_score = game_score[0] if game_score[0] > high_score else high_score
        low_score = game_score[0] if game_score[0] < low_score else low_score
    
    avg_num_of_rounds = (total_rounds//games)
    
    print('')
    print('')
    print('')
    print(f'Played {games} games; Each game ending after 10,000 points or {num_rounds} rounds.')
    print('')
    print(f'Shortest Game: {shortest_game} rounds')
    print(f'Average number of rounds per game: {avg_num_of_rounds}')
    print('')
    print(f'Average Round Score: {total_score//total_rounds}')
    print('')
    print(f'Highest Game Score: {high_score}')
    print(f'Lowest Game Score:  {low_score}')
    print(f'Average Game Score: {total_score//games}')
    print('')
    print('')
    print('')    