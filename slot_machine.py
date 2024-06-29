import random

MAX_NUM_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbols_to_check = column[line]
            if symbol != symbols_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines from 1 - {MAX_NUM_LINES} ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_NUM_LINES:
                break
            else:
                print(f"You must enter number between 1 and {MAX_NUM_LINES} ")
        else:
            print("Please enter a number")

    return lines


def get_bet():
    while True:
        bet = input(f"What would you like to bet on each line ${MIN_BET} - ${MAX_BET} ")
        if bet.isdigit:
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter amount between ${MIN_BET} - ${MAX_BET} ")
        else:
            print("Please enter a number")

    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if balance >= total_bet:
            break
        else:
            print(f"You don't have enough to bet that amount, your current balance is ${balance}")

    print(f"You are betting ${bet} on {lines}. Total amount bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    if winnings != 0:
        print(f"You won on lines", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit) ")
        if answer.lower() == "q":
            break
        elif balance == 0:
            print(f"Insufficient balance! Sorry you can no longer play.")
            break
        balance += spin(balance)

    print(f"You're left with ${balance}")


main()
