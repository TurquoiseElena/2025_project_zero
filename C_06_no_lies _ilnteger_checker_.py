# Functions go here...
def int_check(question):
    """Check that the user enters an integer"""

    error = "Oops - please enter an integer."

    while True:

        try:
            # Check the response to an integer and check that it's more than zero
            response = int(input(question))

            return response

        except ValueError:
            print(error)


while True:
    print()

    # ask user for their name
    name = input("Name: ")  # replace with call to 'not blank' function!

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age < 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")
