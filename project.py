import sys
import re

from random_word import RandomWords
from PyDictionary import PyDictionary
from colorama import Fore, Back, Style

r = RandomWords()
dictionary = PyDictionary()


def main():
    # Introduction text
    print("\nPYDLE\n")
    print("* Try to guess the randomly selected five-letter word within six attempts.")
    print("* Your guesses must be five letters long but do not have to form a real word.")
    print("* Be aware that the word you are looking for is not always in singular or a noun.")
    print("-" * 85)

    # Game
    while True:
        try:
            word = get_word()
            start_round(word)
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()


# Gets a random word, that can be found in the PyDictionary
def get_word():
    print("\nSearching for word...\n")

    while True:
        word = r.get_random_word()
        if word and len(word) == 5:
            if dictionary.meaning(word, disable_errors=True) != None:
                return word


# Starts round
def start_round(word):
    guesses = []
    counter = 6

    while counter > 0:
        guess = input("Guess: ").strip().upper()
        print()

        won, result = check_guess(word, guess)
        if result[0] != "1":
            guesses.append(result)

            for guess in guesses:
                print(*guess)

            print(Style.RESET_ALL)

            if won:
                end_game(True, word)
                break

            counter -= 1

    if counter == 0:
        end_game(False, word)


def check_guess(word, guess):
    word = word.upper()
    guess = guess.upper()
    result = ["1", "2", "3", "4", "5"]

    if check_input(word) and check_input(guess):
        if word == guess:
            for i in range(len(guess)):
                result[i] = Fore.GREEN + guess[i]

            return True, result

        else:
            for i in range(5):
                if word[i] == guess[i]:
                    result[i] = Fore.GREEN + guess[i]
                    word = list(word)
                    word[i] = "0"
                    word = "".join(word)

            for i in range(5):
                if word[i] == "0":
                    pass
                elif guess[i] in word:
                    result[i] = Fore.YELLOW + guess[i]
                else:
                    result[i] = Fore.RESET + guess[i]

    return False, result


def check_input(guess):
    try:
        if re.search(r"^[a-z]{5}$", guess, re.IGNORECASE):
            return True
        else:
            return False
    except ValueError:
        return False
    except TypeError:
        return False


def end_game(won, word):
    if won == True:
        print("You win! Congratulations!\n")
    else:
        print(f"You lost! The word was {word}.\n")

    answer = input(f"Do you wanna see the definition of {word}? yes/no ")
    if answer == "yes":
        print("", "-" * 75, sep="\n")
        print(f"DEFINITION: {word.upper()}\n")
        message = get_definition(word)
        print(*message, end="")
        print("-" * 75, end="\n\n")

    restart = input("Do you wanna play again? yes/no ")
    print()
    if restart != "yes":
        sys.exit()


def get_definition(word):
    definition = dictionary.meaning(word, disable_errors=True)
    message = []

    for key in definition:
        message.append(f"{key}\n")
        for item in definition[key]:
            message.append(f"- {item}\n")
        message.append("\n")

    return message


if __name__ == "__main__":
    main()
