class Solution:
    def longestConsecutive(self, num: List[int]) -> int:
        num=set(num)
        maxLen=0
        while num:
            n=num.pop()
            #l1 for right consective elements total
            #l2 for left (smaller) consecutive element
            l1=0
            l2=0
            
            i=n+1
            #checking and removing elements consecutively higher than n
            while i in num:
                num.remove(i)
                i+=1
                l1+=1
            
            i=n-1
            #checking and removing elements consecutively higher than n
            while i in num:
                num.remove(i)
                i-=1
                l2+=1
                
            #updating maxLen if l1+self+l2 > previous
            maxLen=max(maxLen,l1+l2+1)
            
        return maxLen