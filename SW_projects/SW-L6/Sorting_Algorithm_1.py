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


def main():
    print(set_input_data("test1.csv"))


if __name__ == '__main__':
    main()



