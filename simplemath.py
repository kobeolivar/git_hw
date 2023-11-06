import random

def generate_addition_problem():
    num1 = random.randint(1, 100)  
    num2 = random.randint(1, 100)  
    sum = num1 + num2
    print(f"What is {num1} + {num2}?")
    return sum

def generate_multiplication_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    multiply = num1 * num2
    print(f"What is {num1} * {num2}?")
    return multiply

def get_user_answer():
    try:
        return int(input("Your answer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return get_user_answer()  # Recursive call to prompt again

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is {correct_answer}.")
        raise ValueError("Incorrect answer")

def main():
    # Addition problem
    answer = generate_addition_problem()
    user_answer = get_user_answer()
    check_answer(user_answer, answer)
    
    # Multiplication problem
    answer = generate_multiplication_problem()
    user_answer = get_user_answer()
    check_answer(user_answer, answer)

if __name__ == "__main__":
    main()