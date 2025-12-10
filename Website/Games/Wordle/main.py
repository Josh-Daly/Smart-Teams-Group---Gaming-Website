import random

with open("wordle_wordlist.txt", "r") as f:
    WORD_LIST = [w.strip().lower() for w in f]
    
print(f"Loaded {len(WORD_LIST)} words.")

MAX_GUESSES = 6
WORD_LENGTH = 5

#color codes
ANSI_GREEN = "\033[42m\033[30m"   # green background, black text
ANSI_YELLOW = "\033[43m\033[30m"  # yellow background, black text
ANSI_GRAY = "\033[47m\033[30m"    # white/gray background, black text
ANSI_RESET = "\033[0m"


def pick_secret(words):
    return random.choice(words)


def get_guess(valid_words):
    while True:
        guess = input(f"Enter your guess ({WORD_LENGTH} letters): ").strip().lower()
        if len(guess) != WORD_LENGTH:
            print(f"Please enter exactly {WORD_LENGTH} letters.")
            continue
        if not guess.isalpha():
            print("Only alphabetic letters allowed.")
            continue
        if guess not in valid_words:
            print("Word not in dictionary. Try another word.")
            continue
        return guess


def evaluate_guess(secret, guess):
    status = ["gray"] * WORD_LENGTH
    secret_chars = list(secret)

    for i in range(WORD_LENGTH):
        if guess[i] == secret[i]:
            status[i] = "green"
            secret_chars[i] = None

    remaining_counts = {}
    for ch in secret_chars:
        if ch is not None:
            remaining_counts[ch] = remaining_counts.get(ch, 0) + 1

    for i in range(WORD_LENGTH):
        if status[i] == "gray":
            gch = guess[i]
            if remaining_counts.get(gch, 0) > 0:
                status[i] = "yellow"
                remaining_counts[gch] -= 1

    return status


def print_feedback(guess, status):
    out = []
    for ch, st in zip(guess, status):
        if st == "green":
            out.append(f"{ANSI_GREEN}{ch.upper()}{ANSI_RESET}")
        elif st == "yellow":
            out.append(f"{ANSI_YELLOW}{ch.upper()}{ANSI_RESET}")
        else:
            out.append(f"{ANSI_GRAY}{ch.upper()}{ANSI_RESET}")
    print(" ".join(out))


def play_round(words):
    secret = pick_secret(words)

    for attempt in range(1, MAX_GUESSES + 1):
        print(f"\nGuess {attempt}/{MAX_GUESSES}")
        guess = get_guess(words)
        status = evaluate_guess(secret, guess)
        print_feedback(guess, status)

        if all(s == "green" for s in status):
            print(f"\nCongratulations — you guessed it in {attempt} {'guess' if attempt==1 else 'guesses'}!")
            return True

    print(f"\nOut of guesses. The word was: {secret.upper()}")
    return False


def main():
    print("Welcome to Simple Wordle (5-letter words).")
    print("Colors: green = correct place, yellow = present but wrong place, gray = absent.")
    try:
        while True:
            play_round(WORD_LIST)
            again = input("\nPlay again? (y/n): ").strip().lower()
            if again != "y":
                print("Thanks for playing. Goodbye!")
                break
    except KeyboardInterrupt:
        print("\nBye!")


if __name__ == "__main__":
    main()