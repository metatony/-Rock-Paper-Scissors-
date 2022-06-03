is_running = True

while is_running:

    import random
    print("Let\'s play rock, paper, scissors!")
    R = "rock"
    P = "paper"
    S = "scissor"

    choice_list = [R, P, S]

    user_input = input(
        "What would you like to pick?\n['R', 'P', 'S'] : ")
    if user_input == "R":
        cpu_choice = random.choice(choice_list)
        print("Player(", R, ")", ":", "CPU(", cpu_choice, ")")

        if cpu_choice == R:
            print("Draw")
            continue

        elif cpu_choice == P:
            print("Computer Wins")
            
        elif cpu_choice == S:
            print("Winner")

    elif user_input == "S":
        cpu_choice = random.choice(choice_list)
        print("Player(", S, ")", ":", "CPU(", cpu_choice, ")")

        if cpu_choice == S:
            print("Draw")
            continue

        elif cpu_choice == P:
            print("Winner")

        elif cpu_choice == R:
            print("Computer Wins")

    elif user_input == "P":
        cpu_choice = random.choice(choice_list)
        print("Player(", P, ")", ":", "CPU(", cpu_choice, ")")

        if cpu_choice == P:
            print("Draw")
            continue


        elif cpu_choice == S:
            print("Computer Wins")

        elif cpu_choice == R:
            print("Winner")

    else:
        print("Invalid Entry. Try again")
        continue

    continue_choice = input("Do you wish to continue? [y,n] :")
    if continue_choice == "y":
        pass
    if continue_choice == "n":
        is_running = False
