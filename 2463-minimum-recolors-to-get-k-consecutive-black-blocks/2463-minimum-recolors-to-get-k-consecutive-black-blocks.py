class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        dic = {"W":0,"B":0}
        min_change = float('inf')

        for i in range(k-1):
            dic[blocks[i]]+=1

        left = -1
        for right in range(k-1,len(blocks)):
            if left == -1:
                dic[blocks[right]]+=1

            else:
                dic[blocks[left]]-=1
                dic[blocks[right]]+=1

            min_change = min(min_change, dic["W"])

            left+=1

        return min_change


        

