def duplicate(numbers: list) -> int:
    for i, num in enumerate(numbers):
        while num != i:
            if numbers[num] == num:
                return True, num
            else:
                numbers[i], numbers[num] = numbers[num], numbers[i]
                num = numbers[i]
    return False, None



if __name__ == '__main__':
    print(duplicate([2, 5, 4, 3, 3, 6, 1, 7]))
