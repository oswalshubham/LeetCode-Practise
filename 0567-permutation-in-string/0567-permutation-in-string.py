class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dic = {}

        for char in s1:
            if char not in s1_dic:
                s1_dic[char] = 1
            else:
                s1_dic[char] += 1

        s2_dic = {}
        for i in range(len(s1)-1):
            if s2[i] not in s2_dic:
                s2_dic[s2[i]] = 1
            else:
                s2_dic[s2[i]] += 1

        i=0
        for j in range(len(s1)-1, len(s2)):
            char = s2[j]

            if char not in s2_dic:
                s2_dic[char]=1
            else:
                s2_dic[char]+=1

            if s1_dic == s2_dic:
                return True

            s2_dic[s2[i]]-=1
            if s2_dic[s2[i]] == 0:
                s2_dic.pop(s2[i])
            i+=1

        return False
            
