class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        
        def dfs(depth):
            if depth == len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[depth])
            dfs(depth+1)
            
            subset.pop()
            dfs(depth+1)
            
        
        result = []
        dfs(0)
        return result
        