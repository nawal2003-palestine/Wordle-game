# Wordle-game
Here’s a well-organized **README.md** in English for your Wordle project, complete with colors (using emojis) and examples to make it visually appealing and easy to understand:

---

# **Lab Project 3: Wordle Game**

## **Description**

This project is a **Python implementation** of the popular game **Wordle**, created as part of an educational lab assignment at **ENSAT 2024/2025**. Wordle is a word-guessing game where players have six attempts to guess a five-letter word. Feedback is provided after each guess using colors:

- 🟩 **Green**: The letter is correct and in the right position.  
- 🟨 **Yellow**: The letter is correct but in the wrong position.  
- 🟥 **Red**: The letter is not in the word.

---

## **Features**

The project is modular and divided into several components for better organization:

- **`display.py`**: Manages the game's visuals and feedback display.  
- **`word_choice.py`**: Fetches words from `words.txt` and selects a random word.  
- **`validate_guess.py`**: Validates player inputs to ensure they follow the rules.  
- **`wordle.py`**: Contains the main logic for gameplay and feedback generation.

All valid five-letter words are stored in `wordle_package/assets/words.txt`.

---

## **Project Structure**

```
wordle_game/
├── wordle_package/
│   ├── __init__.py         # Empty file to declare this as a package
│   ├── display.py          # Handles display logic
│   ├── validate_guess.py   # Validates user guesses
│   ├── word_choice.py      # Chooses a random word from the list
│   ├── wordle.py           # Main game logic
│   ├── assets/
│   │   └── words.txt       # Contains the list of valid five-letter words
├── main.py                 # Entry point to run the game
└── README.md               # Project documentation
```

---

## **Installation Instructions**

### **Prerequisites**

- Python 3.8 or later.  
- A terminal or IDE to execute Python scripts.  

### **Steps**

1. Clone this repository to your local machine:  
   ```bash
   git clone https://github.com/your-username/wordle-game.git
   cd wordle-game
   ```

2. Ensure the `words.txt` file contains valid five-letter words, one word per line.  

3. Run the game:  
   ```bash
   python main.py
   ```

---

## **Game Rules**

1. You have **six attempts** to guess the mystery word.  
2. Each guess must be a **valid five-letter word**.  
3. After each guess, the game provides feedback:  
   - 🟩 **Green**: Correct letter in the correct position.  
   - 🟨 **Yellow**: Correct letter, wrong position.  
   - 🟥 **Red**: Incorrect letter.

---

## **Example Gameplay**

Imagine the mystery word is **"apple"**. Here's how a game might progress:

| **Attempt** | **Result**        | **Explanation**                                              |
|-------------|--------------------|--------------------------------------------------------------|
| **grape**   | 🟥 🟨 🟩 🟥 🟥   | "p" is correct and in the right position (🟩). "a" is correct but misplaced (🟨). |
| **plate**   | 🟩 🟩 🟥 🟥 🟥   | "p" and "l" are now in the correct positions (🟩).            |
| **apple**   | 🟩 🟩 🟩 🟩 🟩   | All letters are correct, you win! 🎉                         |

---

## **Customization**

- To add more words, update the `assets/words.txt` file with new five-letter words.  
- Each word must appear on a new line.

---

## **Acknowledgments**

- This implementation is based on the original Wordle game by [Josh Wardle](https://www.powerlanguage.co.uk/wordle/).  
- Created for **ENSAT 2024/2025** as an educational project.
- Naoual Wafiq 

