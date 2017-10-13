
class Recorder(object):

    def __init__(self):
        self.win_loss = list()  #type: list

    def record_win_loss(self, result, player_choice, computer_choice):
        self.win_loss.append((result, player_choice, computer_choice))

    def display_win_loss_record(self, gestures):
        cnt = 1
        print('|{no:<4s}|{result:<7s}|{you:<9s}|{computer:<9s}|'.format(no='No', result='Result', you='You', computer='Computer'))

        for r in self.win_loss:
            print('|{cnt:<4d}|{result:<7s}|{player:<9s}|{computer:<9s}|'.format(cnt=cnt, result=r[0], player=gestures[int(r[1])], computer=gestures[int(r[2])]))
            cnt += 1
