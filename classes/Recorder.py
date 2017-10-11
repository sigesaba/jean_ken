
class Recorder(object):

    def __init__(self):
        self.win_loss = list()  #type: list

    def record_win_loss(self, result, player_choice, computer_choice):
        self.win_loss.append((result, player_choice, computer_choice))
