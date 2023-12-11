class Solution:
    def canFinish(self, numCourses, prerequisites):
        if not prerequisites: return True
        graph = defaultdict(list)

        for f, t in prerequisites:
            graph[f].append(t)

        traced = set()
        visited = set()
        
        def dfs(cur):
            if cur in traced:
                return False
            if cur in visited:
                return True
            
            traced.add(cur)
            for nextNode in graph[cur]:
                if not dfs(nextNode):
                    return False
            
            traced.remove(cur)
            visited.add(cur)
            
            return True
            
        for node in list(graph):
            if not dfs(node):
                return False
        
        return True
                    