class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = defaultdict(list)

        for f, t in prerequisites:
            graph[f].append(t)

        visited = set()
        path = set()

        def dfs(cur):
            if cur in path:
                return False
            if cur in visited:
                return True

            visited.add(cur)
            for nextNode in graph[cur]:
                path.add(cur)
                if not dfs(nextNode):
                    return False
                path.remove(cur)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True