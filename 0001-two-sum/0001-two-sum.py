class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute-force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # using in and slicing
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i+1:]:
                return [i, nums[i+1:].index(complement)+i+1]
                