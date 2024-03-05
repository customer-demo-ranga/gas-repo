# Guess the Number Game

import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: ")) # intentional error, no error handling for non-integer inputs
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

if __name__ == "__main__":
    guess_number()
