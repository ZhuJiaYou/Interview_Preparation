from itertools import permutations


def permutation_str(s):
    ans = set()
    def permutation_nodes(nodes, ps):
        if not nodes:
            ans.add(ps)
            return
        for i in range(len(nodes)):
            tmp = nodes.pop(i)
            permutation_nodes(nodes, ps+tmp)
            nodes.insert(i, tmp)
    permutation_nodes(list(s), "")
    return list(ans)


if __name__ == '__main__':
    s1 = 'abc'
    s2 = 'aacd'
    ans1 = sorted(list(set(''.join(x) for x in permutations(s1))))
    ans2 = sorted(list(set(''.join(x) for x in permutations(s2))))
    print(ans1 == sorted(permutation_str(s1)))
    print(ans2 == sorted(permutation_str(s2)))
