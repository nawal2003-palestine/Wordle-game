import random
from typing import List

# --- Partie 1: Gestion des mots ---
def read_words_file() -> List[str]:
    """Lire les mots depuis le fichier words.txt."""
    filepath = "words.txt"  # Le fichier words.txt doit être dans le même dossier que project.py
    with open(filepath, "r") as file:
        words = file.read().splitlines()
    return words


def choose_random_word(words: List[str]) -> str:
    """Choisir un mot aléatoire."""
    return random.choice(words)

# --- Partie 2: Validation des devinettes ---
def check_guess_valid(guess: str) -> bool:
    """Vérifie si la devinette est un mot valide de 5 lettres."""
    return len(guess) == 5 and guess.islower()

def get_valid_guess(all_words: List[str], guesses: List[str]) -> str:
    """Demander à l'utilisateur une devinette valide."""
    while True:
        guess = input("Entrez un mot de 5 lettres : ").strip()
        if not check_guess_valid(guess):
            print("Format invalide. Entrez un mot de 5 lettres en minuscules.")
        elif guess in guesses:
            print("Vous avez déjà deviné ce mot.")
        elif guess not in all_words:
            print("Le mot n'existe pas dans la liste.")
        else:
            return guess

# --- Partie 3: Gestion des réponses ---
def check_guess_correct(word: str, guess: str) -> bool:
    """Vérifie si la devinette est correcte."""
    return word == guess

def feedback_word(word: str, guess: str) -> List[str]:
    """Retourne un feedback coloré pour la devinette."""
    feedback = ["RED"] * len(guess)
    word_list = list(word)
    for i, letter in enumerate(guess):
        if letter == word_list[i]:
            feedback[i] = "GREEN"
            word_list[i] = None
    for i, letter in enumerate(guess):
        if feedback[i] == "RED" and letter in word_list:
            feedback[i] = "YELLOW"
            word_list[word_list.index(letter)] = None
    return feedback

# --- Partie 4: Affichage ---
COLORS = {"GREEN": "\033[92m", "YELLOW": "\033[93m", "RED": "\033[91m", "RESET": "\033[0m"}

def game_instructions():
    print("Bienvenue dans Wordle!")
    print("Devinez un mot de 5 lettres en 6 essais.")
    print("Feedback:")
    print(f"{COLORS['GREEN']}GREEN{COLORS['RESET']} - Lettre correcte, position correcte.")
    print(f"{COLORS['YELLOW']}YELLOW{COLORS['RESET']} - Lettre correcte, position incorrecte.")
    print(f"{COLORS['RED']}RED{COLORS['RESET']} - Lettre incorrecte.")
    print("Bonne chance!\n")

def display_word_feedback(guess: str, feedback: List[str]) -> str:
    return ''.join(f"{COLORS[color]}{letter}{COLORS['RESET']}" for letter, color in zip(guess, feedback))

def display_win(word: str, attempt: int):
    print(f"Félicitations ! Vous avez deviné le mot '{word}' en {attempt} essais!")

def display_lost(word: str):
    print(f"Dommage ! Le mot était '{word}'. Bonne chance pour la prochaine fois!")

# --- Partie 5: Boucle principale ---
def main():
    game_instructions()
    words = read_words_file()
    target_word = choose_random_word(words)
    attempts = 0
    max_attempts = 6
    previous_guesses = []

    while attempts < max_attempts:
        guess = get_valid_guess(words, previous_guesses)
        previous_guesses.append(guess)
        feedback = feedback_word(target_word, guess)
        print(display_word_feedback(guess, feedback))

        if check_guess_correct(target_word, guess):
            display_win(target_word, attempts + 1)
            break
        attempts += 1
    else:
        display_lost(target_word)

if __name__ == "__main__":
    main()
