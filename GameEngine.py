import Guess

def main():
    guess1 = input("Enter your first guess: ")
    newGuess = Guess.Guess(guess1)
    if newGuess.isNoun:
        if newGuess.isInVector:
            bestGuess = newGuess
    bestGuess = newGuess

    while(True):
        guess2 = input("Enter a new guess: ")
        newGuess2 = Guess.Guess(guess2)
        if newGuess2.isNoun:
            if newGuess2.isInVector:
                if bestGuess.vectorIndex > newGuess2.vectorIndex:
                    bestGuess = newGuess2
                if bestGuess.vectorIndex == 0:
                    print(f"you won! correct guess: {bestGuess}")
                    break
        print(f"current best guess: {bestGuess}, vector index: {bestGuess.vectorIndex} ")

if __name__ == "__main__":
    main()
