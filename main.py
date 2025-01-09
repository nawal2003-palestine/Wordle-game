"""
    This is a python implementation of the Wordle Game.

    Based on the online word game created and developed by Welsh software
    engineer Josh Wardle. Players have six attempts to guess a five-letter word,
    with feedback given for each guess in the form of coloured tiles indicating
    when letters match or occupy the correct position.

    The current version of this project is for education purposes.

    ENSAT 2024/2025.
"""

import random
from typing import List
from wordle_package.display import game_instructions, game_start_display, display_win, display_lost, display_word_feedback
from wordle_package.validate_guess import check_guess_valid, get_valid_guess
from wordle_package.word_choice import read_words_file, choose_random_word
from wordle_package.wordle import check_guess_correct, feed_back_word

def main():
    # Initialize game parameters
    attempt = 0
    previous_guesses = []
    max_attempts = 6

    # Load words from the file and choose a random word
    all_words = read_words_file()
    secret_word = choose_random_word(all_words)

    # Display game instructions and start message
    game_instructions()
    game_start_display()

    # Main game loop
    while attempt < max_attempts:
        print(f"Attempt {attempt + 1}/{max_attempts}.\n")
        
        # Get a valid guess from the user
        guess = get_valid_guess(all_words, previous_guesses)
        previous_guesses.append(guess)
        attempt += 1

        # Check if the guess is correct
        if check_guess_correct(secret_word, guess):
            display_win(secret_word, attempt)
            break

        # Generate and display feedback for the guess
        feedback = feed_back_word(secret_word, guess)
        display_word_feedback(guess, feedback)

    # If the player uses all attempts without guessing the word
    if attempt == max_attempts:
        display_lost(secret_word)
if __name__ == "__main__":
       main()
    
