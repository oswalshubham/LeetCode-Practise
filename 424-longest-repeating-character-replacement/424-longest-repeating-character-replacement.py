class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        maxFreq = 0
        maxLength = 0
        start = 0
        end = 0
        
        while end<len(s):
            if s[end] not in dic:
                dic[s[end]] = 1
            else:
                dic[s[end]]+=1
                
            maxFreq = max(maxFreq, dic[s[end]])
            
            if ((end-start+1)-maxFreq) > k:
                dic[s[start]]-=1
                start+=1
                
            else:
                maxLength = max(maxLength, end-start+1)
                
            
            end+=1
            
        return maxLength
            
        
        