
# 📘 Assignment: Hangman in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Build the Core Game Loop

#### Description
Create a Hangman game where the computer selects a word from a predefined list and the player guesses one letter at a time.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Accept single-letter guesses from the player.
- Display the current word progress using placeholders (for example: `_ _ _ _`).
- Keep the game running until the word is guessed or attempts are exhausted.

### 🛠️ Track Attempts and End States

#### Description
Add win/lose logic and clear game feedback so students can see whether they solved the puzzle in time.

#### Requirements
Completed program should:

- Track and display remaining incorrect guesses after each turn.
- Avoid counting the same incorrect letter twice if guessed again.
- Show a win message when the player guesses the full word.
- Show a lose message with the correct word when attempts run out.
