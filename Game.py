#!/usr/bin/env python
##########################################
#             Guessing game              #
##########################################
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"


import os

tries = 5
myList = ["apple", "banana", "orange", "strawberry", "mango", "watermelon"]


def main():
    global tries
    if tries != 0:
        print("List:")
        print(myList)
        print(f'\n{tries} tries left!')
        guess = input("Guess the last word in the list: ")
        if guess == key:
            myList.append(key)
            print("\nCorrect!\n")
            print(myList)
            print(f'\nYou finished with {tries} tries left!')
            print("")
            input("Press enter to end the game.")
        else:
            os.system('cls')
            print(f"I'm afraid {guess} is not the right anwser!")
            tries -= 1
            main()
    else:
        print(f"Well played! The correct anwser was {key}!")
        myList.append(key)
        print(myList)

if __name__ == '__main__':
    key = "tomato"
    main()