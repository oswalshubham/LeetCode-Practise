class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p=0
        q=1
        
        while q<len(nums):
            if nums[p] != nums[q]:
                p+=1
                nums[p], nums[q] = nums[q], nums[p]
        
            q+=1
            
        return p+1
                