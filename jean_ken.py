from classes.JeanKen import JeanKen
from classes.Recorder import Recorder


def main():
    JeanKen.print_opening_message()
    jean_ken = JeanKen()
    recorder = Recorder()

    while True:
        player_choice = input('Ready? Choose [1]:' + jean_ken.gestures[1] + ', [2]:' + jean_ken.gestures[2] + ', [3]:' + jean_ken.gestures[3] + ', [4]:No Thank you. > ')
        if "4" == player_choice:
            print('Thank you for playing!\n')
            if (len(recorder.win_loss) > 1):

                display_results = input('Would you like to see your results?  [Y/N]: > ')

                if (display_results.upper() == 'Y'):
                    recorder.display_win_loss_record(jean_ken.gestures)

            print('Thank you for playing! See you later!\n')
            break

        try:
            computer_choice = JeanKen.get_computer_choice()  # type: int
            jean_ken.judge(player_choice, computer_choice)
            jean_ken.get_results_in_str()
            recorder.record_win_loss(jean_ken.get_result(), player_choice, computer_choice)

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
