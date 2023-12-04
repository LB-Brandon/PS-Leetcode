class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        if not digits:
            return []
        result = ['']
        for d in digits:
            q = result.copy()
            result = []
            for s in q:
                for c in mapping[d]:
                    result.append(s+c)
                    
        return result
        
    