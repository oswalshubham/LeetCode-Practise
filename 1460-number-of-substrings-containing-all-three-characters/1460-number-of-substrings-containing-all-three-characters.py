class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        dic = {i:0 for i in "abc"}
        n = len(s)
        count = 0
        left = 0

        for right in range(len(s)):
            dic[s[right]]+=1

            while all(dic.values()) > 0:
                count+= n-right

                dic[s[left]]-=1
                left+=1

        return count
        