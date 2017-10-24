from classes.JeanKen import JeanKen
from classes.Recorder import Recorder
from classes.Exporter import Exporter


def main():
    JeanKen.print_opening_message()
    jean_ken = JeanKen()
    recorder = Recorder(10)
    exporter = Exporter()
    print('You can play {0:d} times!'.format(recorder.get_play_limit()))

    while True:
        try:
            player_input = input(
                'Ready? Choose [1]:' + jean_ken.gestures[1] + \
                ', [2]:' + jean_ken.gestures[2] + \
                ', [3]:' + jean_ken.gestures[3] + \
                ', [4]:No Thank you. > ')

            exit_game = True if player_input == '4' else False
            reached_limit = True if recorder.has_reached_to_play_limit() else False

            if exit_game or reached_limit:
                print('Thank you for playing!\n')
                if reached_limit:
                    print('You have played {0:d} times!'.format(recorder.get_play_limit()))

                if (len(recorder.win_loss) > 1):

                    exit_confirmed = confirm('Would you like to see your results?  [Y/N]: > ')
                    if (exit_confirmed):
                        recorder.display_win_loss_record()

                    export_confirmed = confirm('Would you like to export as csv file?  [Y/N]: > ')
                    if (export_confirmed):
                        exporter.export_to_csv(recorder.get_win_loss())

                print('\nThank you for playing! See you later!\n')
                break
            else:
                player_choice = int(player_input)
                jean_ken.validate_player_choice(player_choice)

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


def confirm(confirmation_str):
    while True:
        display_results = input(confirmation_str)

        if (display_results.upper() == 'Y'):
            return True
        elif (display_results.upper() == 'N'):
            return False
        else:
            continue


if __name__ == '__main__':
    main()
