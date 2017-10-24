class Recorder(object):
    def __init__(self, play_times = 10):
        self.win_loss = list()  # type: list
        self.played = 0  # type: int
        self.won = 0  # type: int
        self.lost = 0  # type: int
        self.drew = 0  # type: int
        self.winning_ave = 0  # type: float
        self.play_limit = play_times # type: int

    def has_reached_to_play_limit(self):
        if (self.play_limit <= self.played):
            return True
        else:
            return False

    def get_play_limit(self):
        return self.play_limit

    def get_win_loss(self):
        return self.win_loss

    def record_win_loss(self, gestures, result, player_choice, computer_choice):
        self.played += 1
        if result == 'win':
            self.won += 1
        elif result == 'lose':
            self.lost += 1
        elif result == 'draw':
            self.drew += 1

        self.win_loss.append((result, gestures[int(player_choice)], gestures[int(computer_choice)]))

    def getWinningAve(self, played, won):
        self.winning_ave = won / played
        return self.winning_ave

    def display_win_loss_record(self):
        cnt = 1

        print(
        '\nPlayed: {played:d}, Won: {won:d}, Lost: {lost:d}, Drew: {drew:d}'.format(played=self.played, won=self.won,
                                                                                    lost=self.lost, drew=self.drew))
        print(
            'Your Winning Average is: {winning_ave:.1%}\n'.format(
                winning_ave=self.getWinningAve(self.played, self.won)))
        print('|{no:<4s}|{result:<7s}|{you:<9s}|{computer:<9s}|'.format(no='No', result='Result', you='You',
                                                                        computer='Computer'))

        for r in self.win_loss:
            print('|{cnt:<4d}|{result:<7s}|{player:<9s}|{computer:<9s}|'.format(cnt=cnt, result=r[0],
                                                                                player=r[1],
                                                                                computer=r[2]))
            cnt += 1
        else:
            print()
