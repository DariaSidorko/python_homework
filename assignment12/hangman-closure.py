

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = ''.join([c if c in guesses else '_' for c in secret_word])
        print("Current word:", display)
        return set(secret_word).issubset(set(guesses))

    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").lower()
    print("\n" * 50)  

    guess_func = make_hangman(secret_word)
    all_guessed = False

    while not all_guessed:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        all_guessed = guess_func(guess)

    print(f"\nCongratulations! You guessed the word: {secret_word}")
