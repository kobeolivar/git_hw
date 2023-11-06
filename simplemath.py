import random

def generate_addition_problem():
    num1 = random.randint(1, 100)  
    num2 = random.randint(1, 100)  
    sum = num1 + num2
    print(f"What is {num1} + {num2}?")
    return sum

def main():
    answer = generate_addition_problem()
    user_answer = int(input("Your answer: "))
    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is {answer}.")

if __name__ == "__main__":
    main()
