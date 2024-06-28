import random
import time


OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEM = 10

def generate_problem():
    num_left = random.randint(MIN_OPERAND, MAX_OPERAND)
    num_right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = f"{str(num_left)} {operator} {str(num_right)}"
    answer = eval(expr)
    return expr, answer


input("Press Enter to start ")
print("---------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEM):
    expr, answer = generate_problem()

    while True:
        ans = input(f"Problem #{i + 1}: {expr} = ? ")
        if ans == str(answer):
            print("Correct!")
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("---------------------------")
print(f"Nice work! You finished in {total_time} seconds")
    
