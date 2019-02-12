# ------------- Functions --------------


def ask_number():
    n = 1
    wrong_input = True
    while wrong_input:
        user_input = input('Please type a number: ')
        try:
            n = int(user_input)
            wrong_input = False
        except ValueError:
            print("That's not an integer, try again")
    return n


def test_division(num, den):
    msg = ""
    if den != 0 and num % den == 0:
        msg = ' and Divisible by ' + str(den)
    elif den == 0:
        msg = ". Also, the introduced Denominator equals 0, please introduce another number"
    return msg


def test_even(n, x=4):
    msg = "The introduced Number is "
    if n % 2 == 0:
        msg = msg + 'Even' + test_division(n, x)
    else:
        msg = msg + 'Odd' + test_division(n, x)
    print(msg)

# ------------- Main --------------


test_even(ask_number())

print('\n\nNow we will ask for two numbers:\n')

test_even(ask_number(), ask_number())



