name = input("Type your name: ")
print(f"Welcome, {name}, to the Enchanted Forest Adventure!")

answer = input(
    "You find yourself at a fork in the road. Do you go left towards the mountains or right towards the village? (left/right) "
).lower()

if answer == "left":
    answer = input(
        "You start climbing the mountain and come across a sleeping dragon. Do you try to sneak past or attack it? (sneak/attack) "
    ).lower()
    if answer == "sneak":
        answer = input(
            "You successfully sneak past! You find a mysterious glowing sword. Do you take it or leave it? (take/leave) "
        ).lower()
        if answer == "take":
            print(
                "The sword grants you magical powers! You defeat the dragon when it wakes and become a hero. You win!"
            )
        elif answer == "leave":
            print(
                "You leave the sword and exit the mountain safely, but miss the chance for glory. The end."
            )
        else:
            print(
                "Invalid choice. The dragon wakes up and you run away empty-handed. Game over."
            )
    elif answer == "attack":
        print(
            "The dragon wakes up angry and breathes fire. You barely escape with your life. Game over."
        )
    else:
        print("Not a valid option. You trip and wake the dragon. Game over.")

elif answer == "right":
    answer = input(
        "You arrive at the village market. Do you visit the blacksmith or the tavern? (blacksmith/tavern) "
    ).lower()
    if answer == "blacksmith":
        answer = input(
            "The blacksmith offers to make you a shield or a bow. Which do you choose? (shield/bow) "
        ).lower()
        if answer == "shield":
            print(
                "With your new shield, you defend the village from bandits and become a hero. You win!"
            )
        elif answer == "bow":
            print(
                "With your bow, you hunt and feed the village. Everyone is grateful. You win!"
            )
        else:
            print(
                "Invalid choice. The blacksmith gets annoyed and kicks you out. Game over."
            )
    elif answer == "tavern":
        answer = input(
            "At the tavern, do you listen to rumors or challenge a stranger to a duel? (listen/duel) "
        ).lower()
        if answer == "listen":
            print(
                "You hear about a hidden treasure in the forest and set off to find it. Adventure continues!"
            )
        elif answer == "duel":
            print(
                "The stranger is a master swordsman and defeats you easily. Game over."
            )
        else:
            print(
                "Not a valid option. You spill your drink and get kicked out. Game over."
            )
    else:
        print("Not a valid option. The villagers stare at you suspiciously. Game over.")

else:
    print("Not a valid option. You wander aimlessly until night falls. Game over.")
