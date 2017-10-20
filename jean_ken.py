from classes.JeanKen import JeanKen
from classes.Recorder import Recorder
from classes.Exporter import Exporter


def main():
    JeanKen.print_opening_message()
    jean_ken = JeanKen()
    recorder = Recorder()
    exporter = Exporter()

    while True:
        try:
            player_input = input(
                'Ready? Choose [1]:' + jean_ken.gestures[1] + \
                ', [2]:' + jean_ken.gestures[2] + \
                ', [3]:' + jean_ken.gestures[3] + \
                ', [4]:No Thank you. > ')

            if '4' == player_input:
                print('Thank you for playing!\n')
                if (len(recorder.win_loss) > 1):
                    exit_confirmed = confirm_exit()
                    if (exit_confirmed):
                        recorder.display_win_loss_record()
                        exporter.exportToCSV(recorder.get_win_loss())
                    else:
                        print('\nThank you for playing! See you later!\n')
                break
            else:
                player_choice = int(player_input)
                jean_ken.validatePlayerChoice(player_choice)

                computer_choice = JeanKen.get_computer_choice()  # type: int
                result = jean_ken.judge(player_choice, computer_choice)
                recorder.record_win_loss(jean_ken.gestures, result, player_choice, computer_choice)
                print(
                    '\nRESULT: you {0:s}\n'.format(result.upper()) +
                    'Your hand: {0:s} vs Computer hand: {1:s}\n'.format(jean_ken.gestures[int(player_choice)],
                                                                        jean_ken.gestures[computer_choice])
                )

        except IndexError as e:
            print('{0}'.format(e))
            continue
        except ValueError as e:
            print('Please enter an integer value.')
            continue
        except Exception as e:
            print('{0}'.format(e))
            print('{0}'.format(e.__context__))
            return False

        JeanKen.print_ending_message()

def confirm_exit():
    while True:
        display_results = input('Would you like to see your results?  [Y/N]: > ')

        if (display_results.upper() == 'Y'):
            return True
        elif (display_results.upper() == 'N'):
            return False
        else:
            continue

if __name__ == '__main__':
    main()
