class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        def sol1():
            output = 0
            nums.sort()
            for i in range(0, len(nums), 2):
                output += min(nums[i:i+1])
            return output

        def sol2():
            output = 0
            nums.sort()
            for i in range(len(nums)):
                if i%2 == 0:
                    output += nums[i]
            return output

        def sol3():
            output = sum(sorted(nums)[::2])
            return output

        return sol2()