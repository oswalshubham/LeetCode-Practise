class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        '''
        
        leftminarray = [0]*n
        rightminarray = [0]*n
        leftminarray[0] = nums[0]
        rightminarray[-1] = nums[-1]
        maxscore = 0
            
        for j in range(1,n):
            if nums[j]<leftminarray[j-1]:
                leftminarray[j] = nums[j]
            else:
                leftminarray[j] = leftminarray[j-1]
                
            if nums[n-1-j] < rightminarray[n-j]:
                rightminarray[n-1-j] = nums[n-1-j]
            else:
                rightminarray[n-1-j] = rightminarray[n-j]
                
        print(leftminarray, rightminarray)       
        p=k
        q=k
        
        while p>0:
            while q<n:
                maxscore = max(maxscore, max(rightminarray[p], leftminarray[q])*(q-p+1))
                print(maxscore)
                q+=1
                
            q=k
            p-=1
            
        return maxscore
                
        '''     
            
            
        """
         p right [1,3,3,4,4,5]
         q left [1,1,1,1,1,1]
        
        
         p right [1,1,1,1,1,1,1,1]
        q left [5,5,4,4,4,1,1,1]
        
        
        """
        
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
                
                
        
            
            
                
            
        