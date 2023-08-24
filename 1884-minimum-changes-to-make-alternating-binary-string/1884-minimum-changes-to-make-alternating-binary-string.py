class Solution:
    def minOperations(self, s: str) -> int:

        sone = 0
        szero = 0

        for i in range(len(s)):
            if i%2 == 0:
                if s[i] == "0":
                    sone+=1
                else:
                    szero+=1

            else:
                if s[i] == "0":
                    szero+=1
                else:
                    sone+=1

        return min(szero, sone)

                