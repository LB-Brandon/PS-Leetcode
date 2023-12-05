class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start, path):
            if len(path) == k:
                result.append(path.copy())
                return
            for value in range(start, n+1):
                path.append(value)
                dfs(value+1, path)
                path.pop()
        
        
        result = []
        dfs(1, [])
        return result