#!/usr/bin/env python
###############################################
#  Give one or two words to insert in a list  #
###############################################

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"


def main():
    myList =  ["banana", "apple", "strawberry", "orange"]
    print(myList)
    strs = input("Insert 2 strings (word1 word2): ").split()
    myList.extend(strs)
    print(myList)


if __name__ == '__main__':
    main()
