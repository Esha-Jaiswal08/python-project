import random


def play_game():
    print("=" * 40)
    print("   WELCOME TO THE NUMBER GUESSING GAME")
    print("=" * 40)

    low, high = 1, 100
    secret = random.randint(low, high)
    attempts = 0
    max_attempts = 7

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        guess_input = input(f"Attempt {attempts + 1}/{max_attempts} - Your guess: ")

        if not guess_input.strip().isdigit():
            print("Please enter a valid whole number.\n")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess == secret:
            print(f"\n🎉 Correct! You got it in {attempts} attempt(s)!")
            break
        elif guess < secret:
            print("Too low! Try a higher number.\n")
        else:
            print("Too high! Try a lower number.\n")
    else:
        print(f"\n💀 Out of attempts! The number was {secret}.")


def main():
    play_again = "y"
    while play_again.lower() == "y":
        play_game()
        play_again = input("\nPlay again? (y/n): ")
    print("\nThanks for playing! Goodbye 👋")


if __name__ == "__main__":
    main()
