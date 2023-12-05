class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, path):
            if sum(path) == target:
                result.append(path.copy())
            if sum(path) > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path)
                path.pop()
        
        
        result = []
        dfs(0, [])
        return result