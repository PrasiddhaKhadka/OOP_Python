from random import randint

class RandomGuess:
    currentTries = 0

    def __init__(self, ranNumber):
        print("Welcome to the Random Number Guessing Game")
        self.number = ranNumber

    def guess(self):
        userGuess = int(input("Enter a number between 1 to 100 (or -1 to quit): "))

        if userGuess == -1:
            print(f"You quit! The number was {self.number}. You tried {self.currentTries} times.")
            return

        self.currentTries += 1

        if userGuess == self.number:
            print(f"You won in {self.currentTries} attempts!")
            return
        elif userGuess < self.number:
            print("Your guess was low")
        else:
            print("Your guess was high")

        # Recursively call guess() to ask for input again
        self.guess()

# Generate a random number and start the game
randomNumber = randint(1, 100)
r1 = RandomGuess(randomNumber)
r1.guess()
