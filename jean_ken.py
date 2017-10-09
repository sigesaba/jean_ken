from JeanKen import JeanKen


def main():
    JeanKen.print_opening_message()
    jean_ken = JeanKen()

    while True:
        player_choice = input('Ready? Choose [1]:' + jean_ken.gestures[1] + ', [2]:' + jean_ken.gestures[2] + ', [3]:' + jean_ken.gestures[3] + ', [4]:No Thank you. > ')
        if "4" == player_choice:
            print('Thank you for playing! See you later!\n')
            break

        try:
            jean_ken.set_player_choice(player_choice)
            jean_ken.judge(JeanKen.get_computer_choice())
            jean_ken.get_results_in_str()
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
