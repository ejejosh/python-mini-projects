print("Welcome to this Computer Quiz!"),

playing = input("Do you want to play? Enter (Y) for Yes?\n")

if playing.lower() != "y":
    quit()

print("Okay! Let's play")
score = 0

answer = input("What does CPU stand for?\n")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for?\n")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?\n")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stands for?\n")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score/4 * 100}%.")
