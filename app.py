import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('--------------------')
    print('      JOURNAL-CLI')
    print('--------------------')


def print_menu():
    print('\nChoose one of the options:')
    print('[L]ist entries.')
    print('[A]dd entry.')
    print('[Q]uit.')


def run_event_loop():
    user_cmd = 'no command'
    journal_name = 'default'
    journal_data = journal.load_journal(journal_name)

    while user_cmd != 'q' and user_cmd:
        print_menu()
        user_cmd = input('>')
        user_cmd = user_cmd.lower().strip()

        if user_cmd == 'l':
            list_entries(journal_data)
        elif  user_cmd == 'a':
            add_entry(journal_data)
        elif user_cmd != 'q' and user_cmd:
            print("Sorry, unknown command '{}'.".format(user_cmd.lower().strip()))

    journal.save_journal(journal_name, journal_data)
            

def list_entries(data):
    entries = reversed(data)
    print('Your notes:')
    for index, entry in enumerate(entries):
        print('* [{}] {}'.format(index + 1, entry))


def add_entry(data):
    text = input('Enter your note:')
    data.append(text)


if __name__ == '__main__':
    main()