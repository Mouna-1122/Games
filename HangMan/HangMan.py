import random

# List of words
words = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard",
    "monitor",
    "laptop",
    "internet",
    "science",
    "function"
]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of attempts
attempts = 6

print("=" * 40)
print("Welcome to Hangman!")
print("=" * 40)
print("Guess the word one letter at a time.")

while attempts > 0:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the word
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word!")
        break

    print(f"Attempts Left: {attempts}")

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct Guess!")
    else:
        print("Wrong Guess!")
        attempts -= 1

# Game Over
if attempts == 0:
    print("\nGame Over!")
    print(f"The word was: {secret_word}")