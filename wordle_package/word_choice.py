"""Module for getting all words from words.txt and choosing a random word.

    Functions:
    - read_words_file: Reads all valid 5-letter words from the words.txt file.
    - choose_random_word: Chooses a random word from a list of words.
    
"""


from typing import List
import os

def read_words_file() -> List[str]:
    """Read all valid 5-letter words.
    Return: a list of words strings
    """
    with open(os.path.join("wordle_package", "assets", "words.txt"), "r") as file:
        return [word.strip() for word in file if len(word.strip()) == 5]
    pass


import random
def choose_random_word(words: List[str]) -> str:
    """Choose the starting word for the game.
    Return: a random word on the list
    """
    return random.choice(words)
    pass
