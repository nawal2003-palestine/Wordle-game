"""Module for displaying colored text in the terminal for the Wordle game.

    Functions:
        - header: Prints a header in the terminal.
        - game_instructions: Prints the game instructions in the terminal.
        - game_start_display: Prints the starting message for the game.
        - display_word_feedback: Displays the colored feedback for a guess.

    Constants:
        - COLORS: A dictionary containing ANSI color codes for GREEN, YELLOW, RED, and RESET.
"""


from typing import List

# ANSI color formatting
COLORS = {
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "RED": "\033[31m",
    "RESET": "\033[0m"
}


# def header(text: str) -> None:
#     """Print a header in the terminal."""
#     pass


def game_instructions():
    """Print the game instructions in the terminal."""
    print(f"{COLORS['GREEN']}===Bievenue dans Wordle game!==={COLORS['RESET']}")
    print("Devinez un mots de 5 lettres en 6 essais.")
    print("Feedback:  ")
    print(f"{COLORS['GREEN']}GREEN{COLORS['RESET']} - Lettre correcte, position correcte .")
    print(f"{COLORS['YELLOW']}YELLOW{COLORS['RESET']}  - Lettre correcte, position incorrecte. ")
    print(f"{COLORS['RED']}RED{COLORS['RESET']} - letters incorrecte. ")
    print(f"{COLORS['GREEN']}Bonne chance !{COLORS['RESET']}\n")      
    pass


def game_start_display():
    """Print the starting message for the game."""
    print(f"{COLORS['GREEN']}=== Wordle commence maintenant ! ==={COLORS['RESET']}")
    print("Essayez de deviner le mot secret en 6 tentatives ou moins.\n")
    pass


def display_word_feedback(guess: str, feedback: List[str]) -> str:
    """Display the coloured feedback for a guess."""
    result = ""
    for letter, color in zip(guess, feedback):
        if color == "GREEN":
            result += f"{COLORS['GREEN']}{letter}{COLORS['RESET']}"
        elif color == "YELLOW":
            result += f"{COLORS['YELLOW']}{letter}{COLORS['RESET']}"
        else:
            result += f"{COLORS['RED']}{letter}{COLORS['RESET']}"
    print(result)  # Affiche le feedback dans le terminal
    return result
    pass


def display_win(word: str, attempt: int) -> None:
    """Display for winning"""
    print(f"{COLORS['GREEN']} Félicitation vous avez deviner le mot '{word}' en {attempt} fois {COLORS['RESET']}")
    print("Vous êtes un(e) champion(ne) du Wordle !\n")

    pass


def display_lost(word: str) -> None:
    """Display for losing"""
    print(f"{COLORS['RED']}Dommage ! Vous avez utilisé toutes vos tentatives.{COLORS['RESET']}")
    print(f"Le mot correct était ' {COLORS['GREEN']}{word}{COLORS['RESET']}'. Bonne chance pour la prochaine fois !\n")
    pass










