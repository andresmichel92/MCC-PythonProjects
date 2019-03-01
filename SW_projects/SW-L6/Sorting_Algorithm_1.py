from pathlib import Path
import csv
p = Path('.')

# ===========================
# EX 25 set_input_data method
# ---------------------------


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


def main():

    aList = set_input_data("test1.csv")
    print(aList)
    set_output_data('test2.csv', aList)
    print(execute_merge_sort(aList))


if __name__ == '__main__':
    main()



