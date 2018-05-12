def main():
    print_header()
    run_event_loop()


def print_header():
    print('--------------------')
    print('      JOURNAL-CLI')
    print('--------------------')


def print_menu():
    print('Choose one of the options:\n')
    print('[L]ist entries.')
    print('[A]dd entry.')
    print('[Q]uit.')


def run_event_loop():
    user_cmd = ''
    journal_data = []

    while user_cmd != 'q':
        print_menu()
        user_cmd = input('>')
        user_cmd = user_cmd.lower().strip()

        if user_cmd == 'l':
            list_entries(journal_data)
        elif  user_cmd == 'a':
            add_entry(journal_data)
        elif user_cmd != 'q':
            print("Sorry, unknown command '{}'.".format(user_cmd.lower().strip()))
            

def list_entries(data):
    print(data)


def add_entry(data):
    text = input('Enter your note:')
    data.append(text)


if __name__ == '__main__':
    main()