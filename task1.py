import random

def hangman():
    # Predefined list of words
    words = ["python", "avnish", "rahul", "program", "random"]
    word = random.choice(words)  # Randomly select a word
    guessed_letters = []  # To keep track of guessed letters
    attempts = 6  # Incorrect guesses allowed

    print("🎯 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.")
    print("_ " * len(word))  # Display blanks

    # Game loop
    while attempts > 0:
        guess = input("\nEnter a letter: ").lower()

        # Validation: single alphabet only
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet.")
            continue

        # Already guessed check
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in word:
            print("✅ Good guess!")

        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        # Show progress
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        # Check win
        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("💀 Game Over! The word was:", word)


# Run the game
hangman()
