class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#         subset = []
        
#         def dfs(depth):
#             if depth == len(nums):
#                 result.append(subset.copy())
#                 return
            
#             subset.append(nums[depth])
#             dfs(depth+1)
            
#             subset.pop()
#             dfs(depth+1)

        def dfs(start, path):
            if start > len(nums): return
            
            result.append(path.copy())
            
            for i in range(start, len(nums)):
                dfs(i+1, path+[nums[i]])
                
        result = []
        dfs(0, [])
        return result
        