class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0

        dic = {}
        for i in range(3):
            if s[i] not in dic:
                dic[s[i]]=1
            else:
                dic[s[i]]+=1

        i=0
        count = 0

        for j in range(3,len(s)):

            if len(dic) == 3:
                count+=1

            dic[s[i]] -=1
            if dic[s[i]]==0:
                dic.pop(s[i])

            if s[j] not in dic:
                dic[s[j]]=1
            else:
                dic[s[j]]+=1
            
            i+=1

        if len(dic)==3:
            count+=1

        return count