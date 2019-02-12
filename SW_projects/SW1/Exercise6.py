import Exercise5 as E5


def fibonacci_detector(fibolist):
    response = "This sequence is fibonacci"
    i = 2
    while i < len(fibolist):
        if fibolist[i] != fibolist[i - 1] + fibolist[i - 2]:
            response = "This sequence is not fibonacci"
            break
        i = i + 1
    return response


test = E5.calculate_fibonacci(E5.ask_number())
print(test)
print("is this fibonacci?")

print(fibonacci_detector(test))
print("\n [2,2,2,4,4] \nis this fibonacci?")
print(fibonacci_detector([2, 2, 2, 4, 4]))
