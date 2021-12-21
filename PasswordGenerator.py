#!/usr/bin/env python
##########################################
#        Random password generator       #
##########################################

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

import random, string

def gen_password(characters, numbers):
    password = ''.join((random.choice(string.ascii_letters) for i in range(characters)))  # The amount of characters
    password += ''.join((random.choice(string.digits) for i in range(numbers)))  # The amount of numbers
    myList = list(password)
    random.shuffle(myList) # Shuffle the generated characters
    password = ''.join(myList)
    return password

def main():
    print("1 = Normal password")
    print("1 = Strong password")
    try:
        choice = int(input("Make a choice (1 or 2): "))
    except ValueError:
        print("Please give a number!")
        main()
    if choice == 1:
        print("Normal password:", gen_password(6, 2))

    if choice == 2:
        print("Strong password:", gen_password(7, 4))

    else:
        print("Please choose between 1 or 2!")
        main()

if __name__ == '__main__':
    main()