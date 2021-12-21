#!/usr/bin/env python
##########################################
#             Age Calculator             #
##########################################

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

import datetime

def birthyear(year, age): # Calculate birthyear
    return year - age


def fifty(year, age): # To calculate the year when the person becomes 50
    return year - age + 50

def  main():
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = int(date.strftime("%Y"))
    age = int(input("Age: ")) # Ask for the person's age
    print("You were born in: ", birthyear(year, age))
    print("You are 50 in ", fifty(year, age))

    
if __name__ == '__main__':
    main()