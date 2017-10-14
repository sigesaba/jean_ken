from classes.JeanKen import JeanKen
from classes.Recorder import Recorder


def main():
    JeanKen.print_opening_message()
    jean_ken = JeanKen()
    recorder = Recorder()

    while True:
        try:
            player_input = input(
                'Ready? Choose [1]:' + jean_ken.gestures[1] + ', [2]:' + jean_ken.gestures[2] + ', [3]:' +
                jean_ken.gestures[3] + ', [4]:No Thank you. > ')

            if "4" == player_input:
                print('Thank you for playing!\n')
                if (len(recorder.win_loss) > 1):

                    display_results = input('Would you like to see your results?  [Y/N]: > ')

                    if (display_results.upper() == 'Y'):
                        # recorder.set_score(jean_ken.get_play_count(), jean_ken.get_win_count(), jean_ken.get_lose_count(), jean_ken.get_draw_count())
                        recorder.display_win_loss_record(jean_ken.gestures)

                print('Thank you for playing! See you later!\n')
                break

            player_choice = int(player_input)
            jean_ken.validatePlayerChoice(player_choice)

            computer_choice = JeanKen.get_computer_choice()  # type: int
            result = jean_ken.judge(player_choice, computer_choice)
            recorder.record_win_loss(result, player_choice, computer_choice)
            print(
                'RESULT: you {0:s}\n\n'.format(result) +
                '\nYour hand: {0:s} vs Computer hand: {1:s}\n'.format(jean_ken.gestures[int(player_choice)],
                                                                  jean_ken.gestures[computer_choice])
            )

        except IndexError as ie:
            print(ie.args[0])
            continue
        except ValueError as ve:
            print('Please enter an integer value.')
            continue
        except Exception as e:
            print(e.message)
            return False

        JeanKen.print_ending_message()


if __name__ == '__main__':
    main()
