class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left: int, right: int):
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                    left-=1
                    right+=1
            return s[left+1:right]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        output = ''
        for i in range(len(s)-1):
            output = max(output, expand(i, i+1), expand(i, i+2), key=len)

        return output