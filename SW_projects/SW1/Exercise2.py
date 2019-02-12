from random import *


def generate_random():
    x = randint(1, 9)
    return x


def ask_number():
    n = 1
    wrong_input = True
    while wrong_input:
        user_input = input('Please type your guess: ')
        try:
            n = int(user_input)
            wrong_input = False
        except ValueError:
            print("That's not an integer, try again")
    return n


def guess_game(ran_number):
    print('secret Number:' + str(ran_number))
    quit_game = True
    i = 0
    print('Welcome to the Guess a number game\n where you will have to guess a 1-9 number')
    while quit_game:
        guess = ask_number()
        if guess == ran_number:
            print('SUCCESS!! \n\n')
            quit_game = False
        elif guess > ran_number:
            print('Not quite there yet, you have guessed too high, try again! \n')
            if input("type 'c' to continue, or 'q' to quit the game_ ") == "q":
                quit_game = False
        elif guess < ran_number:
            print('Not quite there yet, you have guessed too low, try again!')
            if input("type 'c' to continue, or 'q' to quit the game_ ") == "q":
                quit_game = False
        i = i + 1
    print('GAME OVER!')
    print("Number of attempts: " + str(i))
    return 0


guess_game(generate_random())


