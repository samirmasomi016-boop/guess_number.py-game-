import random

def play():
    number = random.randint(1, 100)
    attempts = 0
    print("Hello! I have chosen a number between 1 and 100. Try to guess it.")
    while True:
        guess = input("Enter your guess (or 'q' to quit): ")
        if guess.lower() == 'q':
            print("Goodbye!")
            break
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        attempts += 1
        if guess < number:
            print("Too low — try a higher number.")
        elif guess > number:
            print("Too high — try a lower number.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")

if __name__ == "__main__":
    play()
