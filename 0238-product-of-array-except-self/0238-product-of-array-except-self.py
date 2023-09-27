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
            
        # T: O(N), S: O(N)
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
                output.append(pre*post)
            return output

        def sol4():
            output = []
            prefix = []
            postfix = []

            for i in range(len(nums)):
                if i == 0:
                    prefix.append(1)
                else:
                    prefix.append(prefix[-1] * nums[i-1])
            for i in range(len(nums)):
                if i == 0:
                    postfix.append(1)
                else:
                    postfix.append(postfix[-1] * nums[len(nums)-i])
            postfix = postfix[::-1]

            for i in range(len(nums)):
                output.append(prefix[i] * postfix[i])
            return output
        
        def sol5():
            n = len(nums)
            output = [1] * n
            left_product = 1
            right_product = 1

            for i in range(n):
                output[i] = left_product
                left_product *= nums[i]
            print(output)
            for i in range(n-1, -1, -1):
                output[i] = right_product * output[i]
                right_product *= nums[i]
            print(output)
            return output

        
        return sol5()
