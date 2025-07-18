import random

# Initial set up
# ran_num = random.randint(1, 100)
# guessed_num = 0
# while ran_num != guessed_num:
#     guessed_num = input("Guess the number between 1 and 100: ")
#     guessed_num = int(guessed_num)
#     if guessed_num == ran_num:
#         print("Congratulations! You guessed the number!")
#     elif guessed_num < ran_num:
#         print("Too low!")
#     elif guessed_num > ran_num:
#         print("Too high!")
#     else:
#         print("Please enter a valid number")


# allow the user to specify the minimum and maximum values for the number range.
# min_num = input("Specify a min value for the number guessing game: ")
# max_num = input("Specify a max value for the number guessing game: ")
# min_num = int(min_num)
# max_num = int(max_num)
# ran_num = random.randint(min_num, max_num)
# guessed_num = 0
# while ran_num != guessed_num:
#     guessed_num = input(f"Guess the number between {min_num} and {max_num}: ")
#     guessed_num = int(guessed_num)
#     if guessed_num == ran_num:
#         print("Congratulations! You guessed the number!")
#     elif guessed_num < ran_num:
#         print("Too low!")
#     elif guessed_num > ran_num:
#         print("Too high!")
#     else:
#         print("Please enter a valid number")


# A feature that limits the number of guesses, if they run out of attempts, the game ends and the answer is revealed.
# attempts = 5
# ran_num = random.randint(1, 100)
# guessed_num = 0
# while attempts > 0:
#     attempts -= 1
#     guessed_num = input("Guess the number between 1 and 100: ")
#     guessed_num = int(guessed_num)
#     if guessed_num == ran_num:
#         print("Congratulations! You guessed the number!")
#         break
#     elif guessed_num < ran_num:
#         print("Too low!")
#     elif guessed_num > ran_num:
#         print("Too high!")
#     else:
#         print("Please enter a valid number")
# if attempts == 0 and guessed_num != ran_num:
#     print(f"You ran out of attempts, the correct answer is {ran_num}")


# a feature that keeps track of the fewest attempts it took to guess the number correctly
play = input("Do you want to play the number guessing game?(y/n) ").lower()
while play == "y":
    best_score = 100
    ran_num = random.randint(1, 100)
    guessed_num = 0
    attempts = 0
    while ran_num != guessed_num:
        attempts += 1
        guessed_num = input("Guess the number between 1 and 100: ")
        guessed_num = int(guessed_num)
        if guessed_num == ran_num:
            print("Congratulations! You guessed the number!")
            print(f"You made {attempts} attempts in this round")
            if attempts < best_score:
                best_score = attempts
                print(f"You broke your best score, it is now {best_score}!")
        elif guessed_num < ran_num:
            print("Too low!")
        elif guessed_num > ran_num:
            print("Too high!")
        else:
            print("Please enter a valid number")
