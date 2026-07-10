import random

print("====================================")
print("Welcome to the Number Guessing Game!")
print("====================================")

secret_number = random.randint(1, 100)
attempts = 0

print("\nI have selected a number between 1 and 100.")
print("Can you guess it?")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print(" Too high! Try again.")

    else:
        print(f"\n Congratulations! You guessed the number {secret_number}.")
        print(f" You guessed it in {attempts} attempts.")

        play_again = input("\nDo you want to play again? (y/n): ").lower()

        if play_again == "y":
            secret_number = random.randint(1, 100)
            attempts = 0
            print("\n A new number has been generated!")
            continue
        else:
            print("\n Thanks for playing!")
            break