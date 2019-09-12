def can_finish(num_courses, prerequisites):
    indegree = [0] * num_courses
    for pre in prerequisites:
        indegree[pre[0]] += 1
    while prerequisites:
        try:
            now = indegree.index(0)
            indegree.pop(now)
        except ValueError:
            return False
        for i in range(len(prerequisites)):
            if prerequisites[i][1] == now:
                indegree[prerequisites[i][0]] -= 1
        i = 0
        while i < len(prerequisites):
            if indegree[prerequisites[i][0]] == 0:
                prerequisites.pop(i)
            i += 1
        print(indegree)
        print(prerequisites)
    return True

        




if __name__ == '__main__':
    print(can_finish(3, [[1, 0], [1, 2], [0, 1]]))
