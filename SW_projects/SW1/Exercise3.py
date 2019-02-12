def remove_duplicates(list1):
    list2 = []
    i = 0
    while i < len(list1):
        if list2.count(list1[i]) == 0:
            list2.append(list1[i])
        i = i + 1
    return list2


def ask_list():
    string_list = input("Enter list items separated by a comma','")
    list1 = string_list.split(",")
    return list1


lalista = ask_list()
print(lalista)
print(remove_duplicates(lalista))