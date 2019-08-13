from collections import defaultdict
from itertools import repeat


def dice_probability(n, v=6):
    # n is the play times
    # v is the value of the dice
    collects = defaultdict(int)
    collects.update(dict(zip(range(1, 7), repeat(1))))
    for i in range(2, n+1):
        new = defaultdict(int)
        for j in range(i, i*6+1):
            for k in range(1, 7):
            new[j] = sum(collects[j-k] for k in range(1, 7))
        collects = new
    return collects


if __name__ == '__main__':
    print(dice_probability(1, 6))
    print(dice_probability(2, 6))
