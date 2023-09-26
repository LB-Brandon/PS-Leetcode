class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TLE
        def sol1():
            output = []
            for i in range(len(nums)):
                lst = [num for idx, num in enumerate(nums) if idx != i and num != 1]
                total = 1
                for num in lst:
                    total *= num
                output.append(total)
            return output

        # TLE
        def sol2():
            output = []
            for i in range(len(nums)):
                lst = []
                lst.extend(nums[:i])
                lst.extend(nums[i+1:])
                total = 1
                for n in lst:
                    total *= n
                output.append(total)
            return output
            
        def sol3():
            output = []
            prefix = [1] * len(nums)
            postfix = [1] * len(nums)
            init = 1
            for i in range(len(nums)):
                prefix[i] = init*nums[i]
                init = prefix[i]
            init = 1
            for i in range(len(nums)-1, -1, -1):
                postfix[i] = init*nums[i]
                init = postfix[i]
            print('pre', prefix)
            print('post', postfix)
            for i in range(len(nums)):
                pre_idx = i-1
                post_idx = i+1
                if pre_idx < 0:
                    pre = 1
                else:
                    pre = prefix[pre_idx]
                if post_idx >= len(postfix):
                    post = 1
                else:
                    post = postfix[post_idx]
                print(pre, post)
                output.append(pre*post)
            print(output)
            return output

        
        return sol3()
