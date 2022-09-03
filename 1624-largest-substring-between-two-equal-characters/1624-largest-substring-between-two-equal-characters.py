class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = float('-inf')
        
        dic = {}
        
        for i in range(len(s)):
            char = s[i]
            if char not in dic:
                dic[char] = i
                
            else:
                cur_max = i - dic[char] - 1
                result = max(result, cur_max)
                
        return result if result!= float('-inf') else -1
        