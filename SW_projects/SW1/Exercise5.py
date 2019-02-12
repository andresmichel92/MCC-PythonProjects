from math import *

def ask_number():
    n = 1
    wrong_input = True
    while wrong_input:
        user_input = input('Please indicate the number of fibonacci sequence numbers to be calculated: ')
        try:
            n = int(user_input)
            wrong_input = False
        except ValueError:
            print("That's not an integer, try again")
        except n < 0:
            print("That's a negative number, young man, please change it")
    return n


def formula_fibo(n):
    f = 0
    f = int((1/sqrt(5))*(((1+sqrt(5))/2)**(n+1)-((1-sqrt(5))/2)**(n+1)))
    return f


def calculate_fibonacci(number):
    fibo = []
    i = 0
    if number > 0:
        while i <= number:
            fibo.append(formula_fibo(i))
            i = i + 1
    elif number < 0:
        while number <= 0:
            fibo.append(formula_fibo(number))
            number = number + 1
    else:
        print("Something went terribly wrong, run for your life!")
    return fibo


def main():
    print(calculate_fibonacci(ask_number()))


if __name__ == '__main__':
    main()
