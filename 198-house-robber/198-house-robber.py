class Solution:
    def rob(self, nums: List[int]) -> int:
        
        '''
        I rob 1st house only if loot from 1 and 3 is greater than loot from 2
        else I check for next house
        
        '''
        n = len(nums)-1
        def helper(index, memo = {}):
            if index<0:
                return 0
            
            if index in memo:
                return memo[index]
            
            memo[index] = max(helper(index-2, memo)+nums[index], helper(index-1, memo))
            
            return memo[index]
        
        return helper(n)