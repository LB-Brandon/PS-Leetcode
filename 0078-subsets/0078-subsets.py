class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            #decision Not to include nums[i]
            subset.pop()
            dfs(i+1)
        
        result = []
        dfs(0)
        return result
    
#     ----------------------------------------
#     def dfs(start, path):
#             result.append(path)
#             # print(start, start*"  ", path)

#             for i in range(start, len(nums)):
#                 dfs(i+1, path+[nums[i]])

#     result = []
#     dfs(0, [])
#     return result