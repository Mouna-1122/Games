import random

print("Welcome to the Dice Roller Game!")

while True:
    input("\nPress Enter to roll the dice...")

    dice = random.randint(1, 6)
    print(f"You rolled a {dice}!")

    choice = input("\nRoll again? (y/n): ").lower()

    if choice != 'y':
        print("\nThanks for playing!")
        break
