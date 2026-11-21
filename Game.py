
import random

def guessing_game():
    print("\n🎮 WELCOME TO NUMBER GUESSING!")
    print("1. Easy (1-20)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    choice = input("\nChoose difficulty: ")

    levels = {
        "1": (20, 7),
        "2": (50, 6),
        "3": (100, 5)
    }

    if choice not in levels:
        print("Invalid choice!")
        return

    maximum, attempts = levels[choice]
    secret = random.randint(1, maximum)

    print(f"\nGuess a number between 1 and {maximum}!")
    
    while attempts > 0:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if guess == secret:
            print("🎉 YOU WON! Brilliant!")
            return
        elif guess < secret:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")

        attempts -= 1
        print(f"Attempts remaining: {attempts}")

    print(f"\nGame over! The number was {secret}.")

while True:
    guessing_game()
    if input("\nPlay again? (y/n): ").lower() != "y":
        print("Thanks for playing! 👋")
        break
