# Functions go here

# checks users enters either the first letter or
# the full word for a given list, returns full word
def choice_checker(question, valid_list, error):
    valid = False
    while not valid:
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)


# Main Routine starts here

rps_list = ["rock", "paper", "scissors", "xxx"]

while True:
    user_choice = choice_checker("Choose rock / paper / scissors: ",
                                 rps_list, "Please enter rock / paper / scissors")
    print("You chose", user_choice)

    if user_choice == "xxx":
        break
print("we are done")
