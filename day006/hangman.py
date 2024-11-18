import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ["_" for _ in chosen_word]  # Initial display with blanks

lives = 6  # Number of incorrect guesses allowed
end_of_game = False # Negate the initial state of the game

print("Welcome to Hangman Game!")

while not end_of_game: # while the game has not ended! Like while endgame is False
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for index, char in enumerate(chosen_word):
        if char == guess:
            display[index] = char  # Reveal correct guess in display

    # If guessed letter is not in the chosen_word
    if guess not in chosen_word:
        lives -= 1
        print("Incorrect! You lose a life.")

    # Display current progress and remaining lives
    print(" ".join(display))
    print(f"Lives remaining: {lives}")

    # Check if game is over
    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print("Game over! The word was:", chosen_word)
