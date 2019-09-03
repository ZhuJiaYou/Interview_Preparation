def can_complete_circuit(gas, cost):
    now = 0
    go_through = True
    for i in range(len(gas)):
        now = 0
        go_through = True
        for j in range(len(gas)):
            index = (j+i) % (len(gas))
            now += gas[index]
            if cost[index] <= now:
                # print(i, index)
                now -= cost[index]
            else:
                go_through = False
                break;
        if go_through:
            return i
    return -1


def can_complete_circuit2(gas, cost):
    start, overall, rest = 0, 0, 0
    for i in range(len(gas)):
        rest += gas[i] - cost[i]
        overall += gas[i] - cost[i]
        if rest < 0:
            rest, start = 0, i + 1  # NOTICE HERE
    return -1 if overall < 0 else start

        


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(can_complete_circuit2(gas, cost))
    gas  = [2,3,4]
    cost = [3,4,3]
    print(can_complete_circuit2(gas, cost))
