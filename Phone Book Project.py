# Simple phone book program

def add_number(phone_dict, name):
    """Add a new phone number for the given name."""
    try:
        number = int(input(f"Enter the new phone number for {name}: "))
        phone_dict[name] = number
        print(f"The phone number ({number}) for {name} has been added to the database.")
    except ValueError:
        print("Invalid number. Please enter digits only.")

def get_number(phone_dict, name):
    """Retrieve the phone number for the given name."""
    if name in phone_dict:
        return phone_dict[name]
    else:
        print("This name is not in our database.")
        return None

def main():
    phone_dict = {}
    while True:
        question = input("Do you want to use the phone system? (y/n): ").strip().lower()
        if question == 'n':
            break
        print("Choose the next action from the list:")
        print("1) Add a new phone number")
        print("2) Search for a number")
        answer = input("Enter 1 or 2: ").strip()
        if answer == '1':
            name = input("Enter the name for the new phone number: ").strip()
            add_number(phone_dict, name)
        elif answer == '2':
            name = input("Enter the name of the person: ").strip()
            number = get_number(phone_dict, name)
            if number is not None:
                print(f"The phone number for {name} is {number}")
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()