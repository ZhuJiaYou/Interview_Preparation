def find_order(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    visit = [0] * num_courses
    for x, y in prerequisites:
        graph[y].append(x)

    order = []
    def dfs(i):
        nonlocal order
        if visit[i] == -1:  # i is being visited
            return False
        if visit[i] == 1:  # i has been visited, save time
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        order.append(i)
        return True

    for i in range(num_courses):
        if not dfs(i):
            return []
    return order[::-1]


if __name__ == '__main__':
    print(find_order(2, [[1, 0]]))
    print(find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

