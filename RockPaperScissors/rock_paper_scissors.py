import random

choices = ["r", "p", "s"]
choice_names = {"r": "Rock", "p": "Paper", "s": "Scissors"}

while True:
    choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if choice not in choices:
        print("Invalid choice!")
        continue

    comp_choice = random.choice(choices)

    print(f"You chose {choice_names[choice]}")
    print(f"Computer chose {choice_names[comp_choice]}")

    if choice == comp_choice:
        print("It's a tie!")
    elif (
        (choice == "r" and comp_choice == "s")
        or (choice == "p" and comp_choice == "r")
        or (choice == "s" and comp_choice == "p")
    ):
        print("You win!")
    else:
        print("You lose!")

    ans = input("Continue? (y/n): ").lower()
    if ans != "y":
        print("Thanks for playing!")
        break
