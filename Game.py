import random

# List of words
words = ["python", "apple", "computer", "flower", "school"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("====== HANGMAN GAME ======")
print("Guess the word one letter at a time.")
print("You have", max_wrong, "wrong guesses.\n")

while wrong_guesses < max_wrong:

    display = ""

    # Show guessed letters and hide others
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    # Check if word is completed
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)
        print()

# If user loses
if wrong_guesses == max_wrong:
    print("😢 Game Over!")
    print("The correct word was:", word)