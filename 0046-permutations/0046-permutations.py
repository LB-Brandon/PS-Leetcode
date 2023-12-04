class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            # escape
            if len(nums) == 0:
                result.append(path.copy())
                # print('path', path)
                return
        
            for i in range(len(nums)):
                path.append(nums[i])
                newNums = [value for index, value in enumerate(nums) if index != i]
                dfs(newNums, path)
                path.pop()
            

        result = []
        dfs(nums, [])
        return result