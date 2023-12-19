import Guess

def main():
    guess1 = input("Enter your first guess: ")
    newGuess = Guess.Guess(guess1)
    bestGuess = newGuess

    while(True):
        guess2 = input("Enter a new guess: ")
        newGuess2 = Guess.Guess(guess2)
        if newGuess2.get_vector_index() < bestGuess.get_vector_index():
            bestGuess = newGuess2
        print(f"current best guess: {bestGuess}")

if __name__ == "__main__":
    main()