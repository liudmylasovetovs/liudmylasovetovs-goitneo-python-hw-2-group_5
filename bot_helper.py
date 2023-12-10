class InvalidParameterCount(Exception):
    pass


class ContactAlreadyExists(Exception):
    pass


class ContactDoesNotExist(Exception):
    pass


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ContactAlreadyExists:
            return "Contact already exists. Please use change command to update existing contact."
        except InvalidParameterCount:
            return "Invalid parameter count. Please try again using valid parameter count."
        except ContactDoesNotExist:
            return "Contact does not exist. Please use add command to add a new contact."
    return wrapper


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise InvalidParameterCount
    else:
        name, phone = args
        if not (name in contacts):
            contacts[name] = phone
            return "Contact added."
        else:
            raise ContactAlreadyExists


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise InvalidParameterCount
    else:
        name, phone = args
        if not (name in contacts):
            raise ContactDoesNotExist
        contacts[name] = phone
        return "Contact updated."


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise InvalidParameterCount
    else:
        name = args[0]
        if not (name in contacts):
            raise ContactDoesNotExist
    return contacts[name]


@input_error
def show_all(args, contacts):
    if len(args) > 0:
        raise InvalidParameterCount
    for k in contacts:
        print(f"{k}: {contacts[k]}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all(args, contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
