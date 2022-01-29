class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        dic = {}
        n=len(s)
        p=0
        q=0
        while(q<n):
            if s[q] not in dic:
                dic[s[q]] = q
                
            else:   
                
                if p <= dic[s[q]]:
                    p= dic[s[q]]+1
                    dic[s[q]]=q
                else:
                    dic[s[q]] = q
                           
            
            if q-p+1 > maxLength:
                maxLength = q-p+1   
            q+=1
            
        
        return maxLength
        
                    
                
        