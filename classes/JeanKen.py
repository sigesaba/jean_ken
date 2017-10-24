import random


class JeanKen(object):
    def __init__(self):
        self.gestures = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        self.player_choice = ''  # type: int
        self.computer_choice = ''  # type: int
        self.result = ''  # type: str

    def validate_player_choice(self, player_choice):
        if player_choice not in self.gestures:
            raise IndexError('Please enter an integer between 1 to 4')
        else:
            return True

    def judge(self, player_choice, computer_choice):
        self.player_choice = player_choice
        self.computer_choice = computer_choice

        # Judging by deduction:
        # 1 rock     vs paper(2)    : 1-2 = -1 lose
        # 1 rock     vs scissors(3) : 1-3 = -2 win
        # 2 paper    vs scissors(3) : 2-3 = -1 lose
        # 2 paper    vs rock(1)     : 2-1 = 1  win
        # 3 scissors vs rock(1)     : 3-1 = 2  lose
        # 3 scissors vs paper(2)    : 3-2 = 1  win
        if self.computer_choice == self.player_choice:
            return 'draw'
        else:
            value = self.player_choice - self.computer_choice
            if value == -2 or value == 1:
                return 'win'
            elif value == -1 or value == 2:
                return 'lose'

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
