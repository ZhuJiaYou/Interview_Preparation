def cut_rope(length :int) -> int:
    if length == 2:
        return 1
    elif length == 3:
        return 2
    elif length == 4:
        return 4

    time3 = length // 3
    if length - 3 * time3 == 1:
        time3 -= 1
    time2 = (length - 3 * time3) // 2
    return (3 ** time3) * (2 ** time2)


if __name__ == '__main__':
    print(cut_rope(8))
