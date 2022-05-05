class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        '''Try 2'''
        n = len(nums)
        if n==1:
            return nums[0]
        minArray = [0]*n
        minArray[k] = nums[k]
        
        p=k-1
        q=k+1
        
        while p >=0:
            if nums[p] < minArray[p+1]:
                minArray[p] = nums[p]
            else:
                minArray[p] = minArray[p+1]
                
            p-=1
                
        while q<n:
            if nums[q] < minArray[q-1]:
                minArray[q] = nums[q]
            else:
                minArray[q] = minArray[q-1]
                
            q+=1
            
        maxscore = 0
        
        p=0
        q = n-1
        
        
        
        while p<q:
            maxscore = max(maxscore, min(minArray[p],minArray[q])*(q-p+1))
            if minArray[p] <= minArray[q] and p<k:
                p+=1
                
            elif q>k:
                q-=1
                
        return maxscore
                
                
        
            
            
                
            
        
