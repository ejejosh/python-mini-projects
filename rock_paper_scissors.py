import random


player_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit\n").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_num = random.randint(0, 2)

    if user_input == options[random_num]:
        player_wins += 1
        print("You guessed right")
        continue
    else:
        computer_wins += 1
        print(f"Wrong guess! I had {options[random_num]}")
        break

print(f"Your Score: {player_wins}")
print(f"Computer Score: {computer_wins}")
print("Goodbye!")
