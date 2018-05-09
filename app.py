def main():
    print_header()
    run_event_loop()


def print_header():
    print('--------------------')
    print('      JOURNAL-CLI')
    print('--------------------')


def run_event_loop():
    print('Choose one of the options: ')
    user_cmd = None

    while user_cmd != 'q':
        user_cmd = input()

        if user_cmd == 'l':
            print('')
        elif user_cmd == 'a':
            print('')
        elif user_cmd != 'q':
            print("Sorry, unknown command '{}'.".format(user_cmd))



if __name__ == '__main__':
    main()