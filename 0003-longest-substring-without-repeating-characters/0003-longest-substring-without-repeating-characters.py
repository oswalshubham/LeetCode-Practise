class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        a a b a a b ! b b
                p
                  q
        '''
        
        p,q = 0,0
        max_len = -1
        dic = {}

        while q < len(s):
            if s[q] not in dic:
                dic[s[q]] = q
            else:
                max_len = max(max_len, q-p)
                p = max(p,dic[s[q]]+1)
                dic[s[q]] = q

            q+=1

        max_len = max(max_len, q-p)

        return max_len