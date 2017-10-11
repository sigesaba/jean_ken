import random


class JeanKen(object):

    def __init__(self):
        self.gestures = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        self.player_choice = ''  # type: int
        self.computer_choice = ''  # type: int
        self.result = ''  # type: str
        self.playCount = 0
        self.winCount = 0
        self.drawCount = 0

    def set_player_choice(self, player_choice):
        self.player_choice = int(player_choice)
        if self.player_choice not in self.gestures:
            raise IndexError('Please enter an integer between 1 to 4')

    def judge(self, computer_choice):
        self.computer_choice = computer_choice
        self.playCount += 1

        # Judging by deduction:
        # 1 rock     vs paper(2)    : 1-2 = -1 lose
        # 1 rock     vs scissors(3) : 1-3 = -2 win
        # 2 paper    vs scissors(3) : 2-3 = -1 lose
        # 2 paper    vs rock(1)     : 2-1 = 1  win
        # 3 scissors vs rock(1)     : 3-1 = 2  lose
        # 3 scissors vs paper(2)    : 3-2 = 1  win
        if self.computer_choice == self.player_choice:
            self.drawCount += 1
            self.result = 'draw'
        else:
            value = self.player_choice - self.computer_choice
            if value == -2 or value == 1:
                self.winCount += 1
                self.result = 'win'
            elif value == -1 or value == 2:
                self.result = 'lose'

    @staticmethod
    def get_computer_choice():
        return random.randint(1, 3)

    @staticmethod
    def print_opening_message():
        print('\n----------------------')
        print('\nLet\'s Play Rock, Paper, Scissors!')

    @staticmethod
    def print_ending_message():
        print('----------------------\n')

    def get_play_count(self):
        return self.playCount

    def get_win_count(self):
        return self.winCount

    def get_draw_count(self):
        return self.drawCount

    def get_lose_count(self):
        return self.playCount - self.winCount - self.drawCount

    def get_results_in_str(self):
        print(
            '\nYour hand: {0:s} vs Computer hand: {1:s}\n'.format(self.gestures[self.player_choice],
                                                              self.gestures[self.computer_choice]) +
            'RESULT: you {0:s}\n\n'.format(self.result) +
            'You played: {0:d} time(s)\n'.format(self.get_play_count()) +
            'You won: {0:d} time(s)\n'.format(self.get_win_count()) +
            'You lost: {0:d} time(s)\n'.format(self.get_lose_count()) +
            'You drew: {0:d} time(s)'.format(self.get_draw_count())
        )