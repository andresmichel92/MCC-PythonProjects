import Exercise4 as E4

dataset2 = open('Dataset2.txt').read().split(',')
dataset2[len(dataset2)-1] = dataset2[len(dataset2)-1].replace('\n','')
dataset2 = list(map(int, dataset2))
sorted_dataset2 = dataset2
sorted_dataset2.sort()

dataset1 = open('Dataset1.txt').read().split(',')
dataset1[len(dataset1)-1] = dataset1[len(dataset1)-1].replace('\n','')
dataset1 = list(map(int, dataset1))
sorted_dataset1 = dataset1
sorted_dataset1.sort()


def median(lista):
    if len(lista)% 2 == 0:
        h2 = int(len(lista)/2)
        h1 = h2 - 1
        median = (lista[h1] + lista[h2])/2
    else:
        median = lista[int((len(lista)-1)/2)]
    return median


def main():
    print("mean of Dataset1 = " + str(E4.calculate_mean(dataset1)))
    print("standard deviation of Dataset1 = " + str(E4.std_deviation(dataset1)))
    print("median of Dataset1 = " + str(median(dataset1)))
    print("\n")
    print("mean of Dataset2 = " + str(E4.calculate_mean(dataset2)))
    print("standard deviation of Dataset2 = " + str(E4.std_deviation(dataset2)))
    print("median of Dataset2 = " + str(median(dataset2)))

if __name__ == '__main__':
    main()