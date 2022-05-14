import random

# Constant for the possible colors
# colors = "YORPGB"


# Create a secret - a 4-letter word using the possible colors (with duplicates allowed)
def create_secret(colors, code_length):
    secret = ""
    for i in range(code_length):
        secret += colors[random.randrange(len(colors))]
    return secret


# Get a valid guess from the input
def get_guess(colors, code_length):
    guess_is_invalid = True
    while guess_is_invalid:
        guess = input("Make your guess: ").upper()
        if guess == "BOARD":
            guess_is_invalid = False
        if len(guess) == code_length:
            guess_is_invalid = False
            for letter in guess:
                if letter not in colors:
                    guess_is_invalid = True
        if guess_is_invalid:
            print(f" Please write {code_length}-letter words using the characters " +  ", ".join(colors))
    return guess


def display_board(history):

    print()
    for row in history:
        for color in row[0]:
            print(f" {color}", end="")
        print(f" | {row[1]} {row[2]}")
    print()


# Inspect the guess, calculate HITS and CLOSE
def guess_check(guess, secret, code_length, colors):
    hits = 0
    for i in range(code_length):
        if guess[i] == secret[i]:
            hits += 1

    close = 0
    for color in colors:
        close += min(secret.count(color), guess.count(color))
    close = close - hits  
    print(f"Hits: {hits} Close: {close}\n")
    return hits, close


def play_mastermind(colors="YORPGB", code_length=4, number_of_rounds=12):
    #colors = "YORPGB"
    round = 1
    secret = create_secret(colors, code_length)
    history = []
    while round <= number_of_rounds:
        print(f"Round {round}")
        guess = get_guess(colors, code_length)
        if guess == 'BOARD':
            display_board(history)
        else:
            hits, close = guess_check(guess, secret, code_length, colors)
            history.append((guess, hits, close))
            if hits == code_length:
                break
            round += 1
    if hits == code_length:
        print(f"Congratulations, you broke the code! The secret was {secret}.")
    else:
        print(f"You have run out of attempts, you lost the game. The secret was {secret}.")


play_mastermind(colors="YORPGB", code_length=4, number_of_rounds=12)
