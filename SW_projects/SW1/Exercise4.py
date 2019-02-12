from math import *


def calculate_mean(list1):
    mean = sum(list1)/len(list1)
    return mean


def diff_list_sqr(list1, mean):
    i = 0
    list2 = []
    while i < len(list1):
        list2.append((list1[i]-mean)**2)
        i = i + 1
    return list2


def std_deviation(list1):
    std_d = sqrt(calculate_mean(diff_list_sqr(list1, calculate_mean(list1))))
    return std_d

def main():
    lista = [159, 648, 458, 213, 492, 459, 100]
    print("lista: "+str(lista))
    # sdev = std_deviation(lista) for testing results
    print("std deviation " + str(std_deviation(lista)))


if __name__ == '__main__':
    main()

