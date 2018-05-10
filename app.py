def main():
    print_header()
    run_event_loop()


def print_header():
    print('--------------------')
    print('      JOURNAL-CLI')
    print('--------------------')


def run_event_loop():
    print('Choose one of the options:\n')
    print('[L]ist entries.')
    print('[A]dd entry.')
    print('[Q]uit.')
    user_cmd = ''

    while user_cmd != 'q':
        user_cmd = input()
        user_cmd = user_cmd.lower().strip()

        if user_cmd == 'l':
            print('list entries')
        elif  user_cmd == 'a':
            print('add entry')
        elif user_cmd != 'q':
            print("Sorry, unknown command '{}'.".format(user_cmd.lower().strip()))
            



if __name__ == '__main__':
    main()