"""Module for validating input guess.

    Functions:
    - check_guess_valid: Checks if a guess is a valid 5-letter word.
    - get_valid_guess: Gets a valid guess from the user.

"""

from typing import List


def check_guess_valid(guess: str) -> bool:
    """Check if the guess is a valid 5-letter word
    Return: True if the guess is valid, False otherwise
    """
    return len(guess) == 5 and guess.islower()
    pass


def get_valid_guess(all_words: List[str], guesses: List[str]) -> str:
    """Get a valid guess from the user
        Must be:
        1. 5 letter word (lower case)
        2. not previously guessed
        3. exists in words.txt
    """
    while True:
        guess = input("Entrez un mot de 5 lettres : ").strip()
        if not check_guess_valid(guess):
            print("Format invalide . Entrez un mot de 5 lettres en minuscules.")
        elif guess in guesses:
            print("Vous avez déjà deviné ce mot.")
        elif guess not in all_words:
            print("Le mot n'existe pas dans la liste.")
        else:
            return guess
    pass
