#!/usr/bin/env python
##########################################
#           String Transformer           #
##########################################

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

myList = []
def main():
    string = input("String: ") # Ask the user for the string
    text=len(string) # Create a list of characters
    print(f'Inserted string: {string}')
    print(f'Backwards: {string[text::-1]}')
    print(f'Amount of characters: {str(len(string))}')
    myList.append(string)
    print("My List:")
    print(myList)
    main()

if __name__ == '__main__':
    main()
