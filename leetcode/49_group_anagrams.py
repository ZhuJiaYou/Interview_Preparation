from collections import defaultdict


def group_anagrams(arr):
    anagram_dict = defaultdict(list)
    for s in arr:
        anagram_dict["".join(sorted(s))].append(s)

    groups = []
    for v in anagram_dict.values():
        groups.append(v)
    return(groups)


if __name__ == '__main__':
    str_arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(str_arr))
