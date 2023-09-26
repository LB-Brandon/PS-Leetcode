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

        # T: N(N^2), S: N(N^2)
        def two_pointer():
            output = []
            nums.sort()
            if nums[0] > 0: return output
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

        def pos_neg_zero_sum():
            output = set()

            # split nums into three lists
            n, p, z = [], [], []
            for num in nums:
                if num > 0:
                    p.append(num)
                elif num < 0:
                    n.append(num)
                else:
                    z.append(num)
            
            # create a separate set for negatives and positives for O(1) loop-up times
            N, P = set(n), set(p)

            if z:
                for num in P:
                    if -1*num in N:
                        output.add((-1*num, 0, num))
            
            # if there are at least 3 zeros in the list then also include (0, 0, 0) = 0
            if len(z) >= 3:
                output.add((0,0,0))

            # for all pairs of negative numbers(-3, -1), check to see if the complement(4) exists 
            for i in range(len(n)):
                for j in range(i+1, len(n)):
                    target = -1*(n[i]+n[j])
                    if target in P:
                        output.add(tuple(sorted([n[i], n[j], target])))

            # for all pairs of positive numbers, check to see if the complement exists
            for i in range(len(p)):
                for j in range(i+1, len(p)):
                    target = -1*(p[i]+p[j])
                    if target in N:
                        output.add(tuple(sorted([p[i], p[j], target])))
            return output         

        def so():
            output = []

            nums.sort()
            
            # iterate over nums, going over all possible triplets and calculating their sums
            length = len(nums)

            for i in range(length):
                j = i+1
                k = length-1

                while j < k:
                    possibility = sorted([nums[i], nums[j], nums[k]])
                    total = sum(possibility)
                    if total == 0 and i != j and i != k and j != k:
                        if possibility not in output:
                            output.append(possibility)
                        j += 1
                    elif total < 0:
                        j += 1
                    elif total > 0:
                        k -= 1
            return output

        # execute
        return so()