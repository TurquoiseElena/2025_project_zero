# Functions go here...
def yes_no(question):
    """Check thet user enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n). \n")


# Main Routine gose here

# loop for testing purposes...
while True:
    want_instructions = yes_no("Do you eant to read the instructions? ")
    print(f"You chose {want_instructions}\n")