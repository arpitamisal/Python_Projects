print("Welcome to my general knowledge quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Great! Let's get started :)")
score = 0

answer = input("What is the capital of France? ").lower()
if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who wrote 'Romeo and Juliet'? ").lower()
if answer == "william shakespeare":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which planet is known as the Red Planet? ").lower()
if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many continents are there on Earth? ").lower()
if answer == "7" or answer == "seven":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You scored {(score / 4) * 100}%.")

if score == 4:
    print("Excellent! You're a trivia master!")
elif score >= 2:
    print("Not bad! You know some stuff!")
else:
    print("Keep learning! You'll get there :)")
