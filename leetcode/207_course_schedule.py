def can_finish(num_courses, prerequisites):
    indegree = [0] * num_courses
    for pre in prerequisites:
        indegree[pre[0]] += 1
    while prerequisites:
        try:
            now = indegree.index(0)
            indegree[now] = -1
        except ValueError:
            return False
        for i in range(len(prerequisites)):
            if prerequisites[i][1] == now:
                indegree[prerequisites[i][0]] -= 1
        i = 0
        while i < len(prerequisites):
            if indegree[prerequisites[i][0]] == 0:
                prerequisites.pop(i)
            else:
                i += 1
    return True


def can_finish2(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    visit = [0] * num_courses
    for x, y in prerequisites:
        graph[y].append(x)

    def dfs(i):
        if visit[i] == -1:  # i is being visited
            return False
        if visit[i] == 1:  # i has been visited, save time
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True

    for i in range(num_courses):
        if not dfs(i):
            return False
    return True

if __name__ == '__main__':
    print(can_finish2(3, [[2, 0], [2, 1]]))
