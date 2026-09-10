# 🎯 Number Guessing Game

A simple command-line number guessing game written in pure Python — no external
dependencies required.

## How it works

The program picks a random number between 1 and 100. You have 7 attempts to
guess it, and after each guess you're told whether to go higher or lower.

## Requirements

- Python 3.6+
- No third-party packages needed (uses only the built-in `random` module)

## How to run

```bash
python main.py
```

Or on some systems:

```bash
python3 main.py
```

You can also paste `main.py` into any online Python compiler (Replit,
Programiz, OnlineGDB, Pydroid 3, etc.) and run it there.

## Example

```
========================================
   WELCOME TO THE NUMBER GUESSING GAME
========================================

I'm thinking of a number between 1 and 100.
You have 7 attempts. Good luck!

Attempt 1/7 - Your guess: 50
Too high! Try a lower number.

Attempt 2/7 - Your guess: 25
Too low! Try a higher number.
...
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file.
