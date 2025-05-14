import random
import numpy as np

# Mapping card names to values
card_values = {
    "A": 1,
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10
}

# Deck of cards
symbols_list = ["♠", "♥", "♦", "♣"]
denotion_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
mystery_card = [" ___ ", "|   |", "| ⍰ |", "|__ |"]

# Function to print a styled card
def print_card(card):
    for row in card:
        print(row)

# Create a single card as 4 lines of string
def create_card(denotion, symbol):
    top = " ___ "
    middle1 = f"|{denotion:<2} |"
    middle2 = f"| {symbol} |"
    bottom = f"|__{denotion:>2}|"
    return [top, middle1, middle2, bottom]

def user_card(round):
    symbol_1, symbol_2 = random.choice(symbols_list), random.choice(symbols_list)
    denotion_1, denotion_2 = random.choice(denotion_list), random.choice(denotion_list)

    card1 = create_card(denotion_1, symbol_1)
    card2 = create_card(denotion_2, symbol_2)

    if round == 1:
        print("Your cards are:")
        for i in range(4):
            print(card1[i], card2[i])
        return [denotion_1, denotion_2]

    elif round == 2:
        denotion = random.choice(denotion_list)
        symbol = random.choice(symbols_list)
        card = create_card(denotion, symbol)
        print("\nYour card is:")
        print_card(card)
        return denotion

def computer_card(round):
    symbol_1, symbol_2 = random.choice(symbols_list), random.choice(symbols_list)
    denotion_1, denotion_2 = random.choice(denotion_list), random.choice(denotion_list)

    card1 = create_card(denotion_1, symbol_1)
    card2 = create_card(denotion_2, symbol_2)

    if round == 1:
        print("\n\nComputer's cards are:")
        for i in range(4):
            print(card1[i], mystery_card[i])
        return [denotion_1, denotion_2]

    elif round == 2:
        denotion = random.choice(denotion_list)
        symbol = random.choice(symbols_list)
        card = create_card(denotion, symbol)
        print("\n\nComputer's card is:")
        print_card(card)
        return denotion

def convert_to_values(cards):
    numeric = []
    for card in cards:
        if card in ["K", "Q", "J"]:
            numeric.append(10)
        elif card == "A":
            numeric.append(1)
        else:
            numeric.append(int(card))
    return numeric

def calculate_total(cards):
    return np.sum(np.array(convert_to_values(cards)))

print("Welcome to the Black Jack game.")
print("""
Instructions:
✯ When the game starts, you will be given two random cards.
✯ The computer will be assigned to random cards, one of which will not be revealed.
✯ You may choose to obtain another card, where the computer will also be assigned another card.
✯ King, Queen or Jack equals 10.
✯ Whomsoever reaches the number closest to 21 wins.
✯ If you reach a number greater than 21, you lose.""")

input("Click enter to start the game.")

continue_game = True

while continue_game:
    user_print_list = []
    computer_print_list = []

    user_values = user_card(1)
    computer_values = computer_card(1)

    user_print_list.extend(user_values)
    computer_print_list.extend(computer_values)

    user_value = calculate_total(user_values)
    computer_value = calculate_total(computer_values)

    while True:
        choice = input("\nTry getting another card? (y/n): ").lower()
        if choice == 'y':
            extra_user_value = user_card(2)
            extra_computer_value = computer_card(2)

            user_print_list.extend([extra_user_value])
            computer_print_list.extend([extra_computer_value])

            user_value = calculate_total(user_print_list)
            computer_value = calculate_total(computer_print_list)

            if user_value >= 21 or computer_value >= 21:
                break
        else:
            break

    print("\nYour card values are:", user_print_list)
    print("Computer's card values are:", computer_print_list)

    print("\nThe total value you've got:", user_value)
    print("The total value computer's got:", computer_value)

    if user_value <= 21 and computer_value > 21:
        print("You win!")
    elif computer_value <= 21 and user_value > 21:
        print("Computer wins!")
    elif user_value == computer_value:
        print("It is a draw!")
    elif user_value <= 21 and computer_value <= 21:
        if user_value > computer_value:
            print("You win!")
        else:
            print("Computer wins!")

    choice = input("\nPlay another game? (y/n): ").lower()
    continue_game = (choice == 'y')

print("Thanks for playing! Goodbye!")
