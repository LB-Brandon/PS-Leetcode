class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(i: int, cur: List[int]):
            if i == len(nums):
                ans.append(cur.copy())
                return

            dfs(i+1, cur)
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.remove(nums[i])

        dfs(0, [])
        return ans