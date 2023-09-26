class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        def sol1():
            output = 0
            nums.sort()
            for i in range(0, len(nums), 2):
                output += sum(nums[i:i+1])
            return output
        return sol1()