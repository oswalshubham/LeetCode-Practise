class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        answer = ""

        def checkPalindrome(i,j, result):
            count = len(result)
            while i>=0 and j < len(s):
                if s[i] != s[j]:
                    break
                
                else:
                    if j-i+1 > count:
                        count = j-i+1
                        result = s[i:j+1]
                    

                i-=1
                j+=1

            return result

        
        for i in range(len(s)-1):
            single_check = checkPalindrome(i,i, "")
            print(single_check)
            double_check = checkPalindrome(i,i+1, single_check)
            print(double_check)
            if len(double_check) > len(answer):
                answer = double_check

        return answer

