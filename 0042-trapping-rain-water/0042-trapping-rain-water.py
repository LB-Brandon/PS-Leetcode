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
                
                
        # two pointer
        def two_wall():
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
        
        return BF()

                
            
