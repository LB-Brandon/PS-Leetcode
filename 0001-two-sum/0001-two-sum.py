class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def bf():
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
            return []

        def in_slicing():
            for i, num in enumerate(nums):
                complement = target - num
                if complement in nums[i+1:]:
                    return [i, nums[i+1:].index(complement)+i+1]

        def map():
            nums_map = {}
            for i, num in enumerate(nums):
                nums_map[num] = i
            for i, num in enumerate(nums):
                if target - num in nums_map and i != nums_map[target-num]:
                    return [i, nums_map[target-num]]
            return []

        # excute
        return map()
                