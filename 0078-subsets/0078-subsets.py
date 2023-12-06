class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(start, path):
            result.append(path)
            # print(start, start*"  ", path)

            for i in range(start, len(nums)):
                dfs(i+1, path+[nums[i]])

        result = []
        dfs(0, [])
        return result