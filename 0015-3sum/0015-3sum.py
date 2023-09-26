class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # T:O(N^3), S:O(N^3), TLE
        def BF():
            output = set()
            n = len(nums)
            for i in range(n):
                for j in range(i+1, n):
                    for k in range(j+1, n):
                        total = nums[i] + nums[j] + nums[k]
                        if total == 0:
                            output.add(tuple(sorted([nums[i], nums[j], nums[k]])))
            output = list(map(list, output))
            return output

        # T:O(N^3), S:O(N^3), TLE
        from itertools import combinations
        def using_combination():
            output = set()
            n = len(nums)
            for comb in combinations(nums, 3):
                if sum(comb) == 0:
                    output.add(tuple(sorted(comb)))
            output = list(output)
            return output

        def two_pointer():
            output = []
            nums.sort()
            
            for i in range(len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                left, right = i+1, len(nums)-1
                while left < right:
                    total = nums[i]+nums[left]+nums[right]
                    if total < 0:
                        left += 1
                    elif total > 0:
                        right -= 1
                    else:
                        output.append([nums[i], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
            return output
            print(output)




        # excute
        return two_pointer()