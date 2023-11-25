def input_error(foo):
    def wrapper(*args):
        try:
            return foo(*args)
        except KeyError:
            print("There is no such record in the book")
        except IndexError:
            print("Invalid number of parameters passed to the command")
        except TypeError as te:
            if 'handle_add() takes 3 positional arguments but' in str(te):
                print('Too many arguments')
            elif 'handle_add() missing 1 required positional argument:' in str(te):
                print('Give me phone please')
        #print("Invalid number of parameters passed to the command")
    return wrapper
@input_error
def handle_add(book, name, phone):
    if not name in book.keys():
        if not name.isalpha():
            print('Name must contains only letters')
        else:
            if not phone.isdigit():
                print('Phone must contains only digits')
            else:
                book[name] = phone
        return book
    else:
        print('This name already exists')
@input_error
def handle_read(book, name):
    print(book[name])
@input_error
def handle_change(book, name, phone):
    if not name in book.keys():
        raise KeyError()
    if not phone in book.values():
            if phone == '':
                print('type a number please')
            else:
                book[name] = phone
    else:
        print('This number already exist in Phone Book')
    return book
@input_error
def handle_show_all(book):
    for key, value in book.items():
        print(f"{key}: {value}")
def main():
    contact_book = {}
    while True:
        choice = input()
        if choice == 'show all': #5
            handle_show_all(contact_book)
        if choice in ['exit', 'close', 'good bye']: #6
            print('Good bye!')
            break
        words = choice.split(' ')
        command = words[0].lower()
        if command not in ['hello', 'add', 'change', 'phone', 'show all', 'exit', 'close', 'good bye', 'FAQ' ]:
            print('Wrong command. Use the "FAQ" for read Manual')
        args = words[1:]
        if command == 'hello':    #1 hello
            print('How canI help you?')
        elif command == 'FAQ':
            print('-' * 100 + '\n'
                  'You can Add using command-> "add" new item in Phone Book, \n'
                  'Change using command-> "change" the item in Phone Book,\n'
                  'Show the phone by the name of Contact that stored in the Phone Book using command-> "phone",\n'
                  'Show all items in the Phone Book command-> "show all",\n'
                  'Close the Phone Book using command-> "good buy", "close", "exit"\n' +
                  '-' * 100 + '\n')
        elif command == 'add':
            handle_add(contact_book, *args) #2 add
        elif command == 'change':
            handle_change(contact_book, *args)  #3 change
        elif command == "phone":
            handle_read(contact_book, *args)    #4 phone
        elif command in ['exit', 'close', 'good bye']:
            break
if __name__ == "__main__":
    main()