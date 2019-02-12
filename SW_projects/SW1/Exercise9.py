
units = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"], ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"], ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "MC"],["", "M", "MM", "MMM"]]


def small_romans(list1):
    roman = ""
    smallr = []
    i = len(list1) - 1
    # print("i="+str(i))
    j = 0
    while i >= 0:
        # print("j="+str(j)+" units[j]="+ str(units[j]))
        smallr.append(units[j][int(list1[i])])
        j = j + 1
        i = i - 1
    smallr.reverse()
    roman = ''.join(smallr)
    return roman


def large_romans(list1):
    larger = ""
    lines = ""
    n = len(list1)
    small_part = list1[n-3] + list1[n-2] + list1[n-1]
    last_half = small_romans(small_part)
    large_part = list1[:n-3]
    first_half = small_romans(large_part)
    for i in first_half:
        lines = lines+"_"
    roman = lines + "\n" + first_half + last_half
    return roman


def generate_romans(num):
    roman = ""
    lista = list(str(num))
    if num == 1000000:
        roman = "_\nM"
    elif 0 < num < 4000:
        roman = small_romans(lista)
    elif 3999 < num < 1000000:
        roman = large_romans(lista)
    else:
        roman = "not valid number, needs to be positive and less than 1'000,001"
    return roman


def ask_number():
    n = 1
    wrong_input = True
    while wrong_input:
        user_input = input("Please type the number you'd like to convert: ")
        try:
            n = int(user_input)
            wrong_input = False
        except ValueError:
            print("That's not an integer, try again")
    return n


def main():
    print("Roman numerals generator\n")
    print(generate_romans(ask_number()))


if __name__ == "__main__":
    main()

# the rule is that we can concatenate units, tents, and centimals up to three times. Then we substract one, and concatenate 3 afterwards