import random

# Constant for the possible colors
colors = "YORPGB"

# Create a secret - a 4-letter word using the possible colors (with duplicates allowed)
secret = ""
for i in range(4):
    secret += colors[random.randrange(6)]
history = []
secret = "YYPP"
# Start the game
round = 1
while round <= 12:
    print(f"Round {round}")

    # Get a valid guess from the input
    guess_is_invalid = True
    while guess_is_invalid:
        guess = input("Make your guess: ").upper()
        if guess == "BOARD":
            guess_is_invalid = False
        if len(guess) == 4:
            guess_is_invalid = False
            for letter in guess:
                if letter not in colors:
                    guess_is_invalid = True
        if guess_is_invalid:
            print(" Please write 4-letter words using the characters Y, O, R, P, G, B!")

    if guess == 'BOARD':
        print()
        for row in history:
            for color in row[0]:
                print(f" {color}", end="")
            print(f" | {row[1]} {row[2]}")
        print()
    else:
        # Inspect the guess, calculate HITS and CLOSE
        hits = 0
        for i in range(4):
            if guess[i] == secret[i]:
                hits += 1

        close = 0
        for color in colors:
            close += min(secret.count(color), guess.count(color))
        close = close - hits  # Don't count HITS again

        print(f"Hits: {hits} Close: {close}\n")
        history.append((guess, hits, close))
        if hits == 4:
            break
        round += 1

if hits == 4:
    print(f"Congratulations, you broke the code! The secret was {secret}.")
else:
    print(f"You have run out of attempts, you lost the game. The secret was {secret}.")
