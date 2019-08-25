def plus_one(digits):
    carry, digits[-1] = (digits[-1] + 1)//10, (digits[-1] + 1)%10
    i = len(digits) - 2
    while carry != 0 and i >= 0:
        carry, digits[i] = (digits[i] + carry)//10, (digits[i] + carry)%10
        i -= 1
    if i < 0 and carry != 0:
        digits.insert(0, carry)
    return digits


if __name__ == '__main__':
    digits = [9, 9, 9]
    print(plus_one(digits))
