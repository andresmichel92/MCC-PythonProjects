from pathlib import Path
import csv
import time
from copy import deepcopy

data = []
# ===========================
# EX 25 set_input_data method
# ---------------------------


def generate_data(list_to_sort, start_time):
    data.clear()
    data.append("Size: ")
    data.append(len(list_to_sort))
    data.append("Start time: ")
    data.append(start_time)
    data.append("End_time: ")


def generate_end_data(starting):
    end = time.time()
    data.append(end)
    duration = end - starting
    data.append("Duration: ")
    data.append(duration)


def set_input_data(file_path_name):
    f_list = []
    with open(file_path_name, 'r') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
        try:
            f_list = [float(i) for i in csv_list[0]]
        except ValueError:
            print("One or more non-numeric values have been found in your data set, please try again")
    return f_list


def set_output_data(file_path_name, sorted_list):

    # sorted_list = map(str, sorted_list)
    with open(file_path_name, 'w') as my_file:
        wr = csv.writer(my_file, delimiter=',', quoting=csv.QUOTE_ALL)
        wr.writerow(sorted_list)


def execute_merge_sort(unsorted_list):
    start = time.time()
    generate_data(unsorted_list, start)
    if len(unsorted_list) > 1:
        mid = int(len(unsorted_list)/2)
        right_half = unsorted_list[:mid]
        left_half = unsorted_list[mid:]

        execute_merge_sort(right_half)
        execute_merge_sort(left_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                unsorted_list[k] = left_half[i]
                i = i + 1
            else:
                unsorted_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            unsorted_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            unsorted_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    return unsorted_list


def execute_quick_sort(unsorted_list):
    lista = deepcopy(unsorted_list)
    splitter(lista, 0, len(lista)-1)
    return lista


def splitter(lista, first, last):

    if first < last:
        splitpoint = partition(lista, first, last)
        splitter(lista, first, splitpoint-1)
        splitter(lista, splitpoint+1, last)


def partition(lista, first, last):
    pivotvalue = lista[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and lista[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while lista[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = lista[leftmark]
            lista[leftmark] = lista[rightmark]
            lista[rightmark] = temp

        temp = lista[first]
        lista[first] = lista[rightmark]
        lista[rightmark] = temp

    return rightmark


def execute_heap_sort(unsorted_list):
    aList=deepcopy(unsorted_list)
    # convert aList to heap
    length = len(aList) - 1
    leastParent = length / 2
    for i in range(int(leastParent), -1, -1):
        moveDown(aList, i, length)

    # flatten heap into sorted array
    for i in range(length, 0, -1):
        if aList[0] > aList[i]:
            swap(aList, 0, i)
            moveDown(aList, 0, i - 1)
    return aList


def moveDown(aList, first, last):
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if (largest < last) and (aList[largest] < aList[largest + 1]):
            largest += 1

        # right child is larger than parent
        if aList[largest] > aList[first]:
            swap(aList, largest, first)
            # move down to largest child
            first = largest
            largest = 2 * first + 1
        else:
            return  # force exit


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def main():

    unaList = set_input_data("test1.csv")
    #print(aList)
    #set_output_data('test2.csv', unaList)
    print(execute_merge_sort(unaList))
    generate_end_data(data[3])
    print(data)
    print(len(data))
    #print(execute_heap_sort(unaList))


if __name__ == '__main__':
    main()



