import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)

    # Blackjack
    if score == 21 and len(hand) == 2:
        return 0

    # Ace adjustment
    while score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score

def compare(user_score, computer_score):

    if user_score == computer_score:
        return "It's a Draw!"

    elif computer_score == 0:
        return "Computer has Blackjack. You Lose!"

    elif user_score == 0:
        return "Blackjack! You Win!"

    elif user_score > 21:
        return "You went over 21. You Lose!"

    elif computer_score > 21:
        return "Computer went over 21. You Win!"

    elif user_score > computer_score:
        return "You Win!"

    else:
        return "Computer Wins!"

print("=" * 40)
print("        BLACKJACK GAME")
print("=" * 40)

while True:

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards} | Score: {user_score if user_score != 0 else 21}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("\nDo you want another card? (y/n): ").lower()

            if choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("\n" + "=" * 40)
    print(f"Your final hand     : {user_cards} | Score: {user_score if user_score != 0 else 21}")
    print(f"Computer final hand : {computer_cards} | Score: {computer_score if computer_score != 0 else 21}")
    print("=" * 40)

    print(compare(user_score, computer_score))

    play_again = input("\nPlay Again? (y/n): ").lower()

    if play_again != "y":
        print("\nThanks for playing!")
        break