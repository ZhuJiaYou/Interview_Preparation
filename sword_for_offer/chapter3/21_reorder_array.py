import random


def reorder_array(array):
    i = 0
    j = len(array) - 1
    while i < j:
        if array[i] % 2 == 0 and array[j] % 2 == 1:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        if array[i] % 2 == 1:
            i += 1
        if array[j] % 2 == 0:
            j -= 1


if __name__ == '__main__':
    array = list(range(15))
    random.shuffle(array)
    print(array)
    reorder_array(array)
    print(array)
