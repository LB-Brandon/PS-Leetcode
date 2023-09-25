class Solution:
    def trap(self, height: List[int]) -> int:

        def BF():
            output = 0
            # can't use max() for empty list
            for i in range(1, len(height)-1):
                left_max = max(height[:i])
                right_max = max(height[i+1:])

                min_height = min(left_max, right_max)
                if min_height > height[i]:
                    output += min_height - height[i]
            return output
                
        def two_pointer():
            left, right = 0, len(height)-1
            left_max, right_max = height[left], height[right]
            output = 0
            while left < right:
                left_max = max(left_max, height[left])
                right_max = max(right_max, height[right])
                if left_max <= right_max:
                    output += left_max - height[left]
                    left += 1
                else:
                    output += right_max - height[right]
                    right -= 1
            return output

        # T: O(n), S: O(n), two additinal lists of size N are used.
        def pre_processing():
            # don't declare a variable like "left = right = []"
            left_max_values, right_max_values = [], []
            left_max = right_max = 0
            output = 0

            for i in range(len(height)):
                left_max_values.append(left_max)
                right_max_values.append(right_max)
                if left_max < height[i]:
                    left_max = height[i]
                if right_max < height[-i-1]:
                    right_max = height[-i-1]
            right_max_values = right_max_values[::-1]

            for i in range(len(left_max_values)):
                min_val = min(left_max_values[i], right_max_values[i])
                if min_val - height[i] > 0:
                    output += min_val - height[i]
            return output

        def using_stack():
            stack = []
            output = 0
            for i in range(len(height)):
                while stack and height[i] > height[stack[-1]]:
                    top = stack.pop()
                    if not stack:
                        break
                    distance = i - stack[-1] - 1
                    bounded_height = min(height[i], height[stack[-1]]) - height[top]
                    output += distance * bounded_height
                stack.append(i)
            return output

                
                
        
        return using_stack()

                
            
