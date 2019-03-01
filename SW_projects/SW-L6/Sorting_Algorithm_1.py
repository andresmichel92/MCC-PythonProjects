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


def main():

    aList = set_input_data("test1.csv")
    print(aList)
    set_output_date('test2.csv', aList)




if __name__ == '__main__':
    main()



