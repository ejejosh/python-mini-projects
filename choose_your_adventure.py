name = input("Enter your name:\n")
print(f"Welcome {name}, to this adventure")

answer = input("You're on a dirt road, it has come to an end and you can either go LEFT or RIGHT. Which way would you"
               " like to go? ").lower()

if answer == "left":
    answer = input("You've come to a river, you can either walk around it or swim across. Type WALK to walk around or "
                   "SWIM to swim across\n")
    if answer == "swim":
        print("You swim across and were eaten by an Alligator")
    elif answer == "walk":
        print("You walked many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You've come to a bridge it looks wobbly, do you like to cross it or head back (Cross/Back)?\n")

    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (Yes/No)?\n")
        if answer.lower() == "yes":
            print("You talk to the stranger and they gave you Silver and Gold. You WIN!")
        elif answer.lower() == "no":
            print("You ignore the stranger and they are offended and you lose")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option, You lose")

print("Thank you for playing. Goodbye!")
