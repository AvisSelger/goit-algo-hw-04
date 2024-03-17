def parse_input(user_input):
    """
    Parses the user input into command and arguments.

    :param user_input: A string input by the user.
    :return: A tuple containing the command and a list of arguments.
    """
    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def add_contact(args, contacts):
    """
    Adds a new contact to the contacts dictionary.

    :param args: A list of arguments, where args[0] is the name and args[1] is the phone number.
    :param contacts: The dictionary where contacts are stored.
    :return: A string message indicating the result.
    """
    if len(args) != 2:
        return "Error: Invalid number of arguments for add command."
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Changes the phone number of an existing contact.

    :param args: A list of arguments, where args[0] is the name and args[1] is the new phone number.
    :param contacts: The dictionary where contacts are stored.
    :return: A string message indicating the result.
    """
    if len(args) != 2:
        return "Error: Invalid number of arguments for change command."
    name, new_phone = args
    if name.lower() in contacts:
        contacts[name.lower()] = new_phone
        return "Contact updated."
    else:
        return "Error: Contact not found."

def show_phone(args, contacts):
    """
    Shows the phone number of a contact.

    :param args: A list of arguments, where args[0] is the name.
    :param contacts: The dictionary where contacts are stored.
    :return: A string message indicating the result.
    """
    if len(args) != 1:
        return "Error: Invalid number of arguments for phone command."
    name = args[0].lower()
    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact not found."

def show_all(_, contacts):
    """
    Shows all contacts and their phone numbers.

    :param _: Ignored.
    :param contacts: The dictionary where contacts are stored.
    :return: A string containing all contacts and their phone numbers.
    """
    if contacts:
        return "\n".join([f"{name.title()}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

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
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
