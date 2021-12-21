#!/usr/bin/env python
##########################################
#               Calculator               #
##########################################

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"


# Plus
def plus(x, y):
    return x + y


# Minus
def minus(x, y):
    return x - y


# Times
def times(x, y):
    return x * y


# Devide
def devide(x, y):
    return x / y


print("1.Plus")
print("2.Min")
print("3.Maal")
print("4.Delen door")


def main():
    while True:
        try:
            choice = input("Make a choice (1/2/3/4): ")
        except ValueError:
            print("Please insert a number.")
            main()

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", plus(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", minus(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", times(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", devide(num1, num2))
            break
        else:
            print("please choose a number between 1 and 4.")
            main()


if __name__ == '__main__':
    main()
