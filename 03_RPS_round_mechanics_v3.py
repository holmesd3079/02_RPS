# functions go here

def check_rounds():
    while True:
        response = input("RPS: How many rounds would you like to play: ")
        round_error = "Type either <enter> or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue
        return response


# main routine goes here

round_played = 0
choose_instructions = "Please choose Rock (r) Paper (p) or Scissors (s)"

# ask user for # rounds, <enter> to have infinite rounds
rounds = check_rounds()

end_game = "no"

while end_game == "no":

    print()
    if rounds == "":
        heading = f"Continuous Mode: Round {round_played}"
        print(heading)
        choose = input(f"{choose_instructions} or 'xxx' to end")
        if choose == "xxx":
            break
    else:
        heading = f"Round {round_played + 1} out of {rounds} "
        print(heading)
        choose = input(choose_instructions)
        if round_played == rounds - 1:
            end_game = "yes"
        print(f"You choose {choose}")
        round_played += 1
print("Unthank you for playing")
# Rounds heading

# https://youtu.be/Ky-kkwLj0XE?list=PLwll6mdTmnFG1iyG4nr16g60mLKbzo7rx&t=93
