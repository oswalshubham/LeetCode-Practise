class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target:
            return 0
        
        p=start - 1
        q = start + 1
        
        while q < len(nums) or p >= 0:
            if q < len(nums):
                if nums[q] == target:
                    return abs(start - q)
                else:
                    q+=1
                    
            if p>=0:
                if nums[p] == target:
                    return abs(start - p)
                else:
                    p-=1
                    
                    
        
        