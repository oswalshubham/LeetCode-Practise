class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n= len(nums)
        right_average = [0]*n
        left_average = [0]*n
        left_sum,right_sum = 0,0
        minAvgDiff = float('inf')
        
        for i in range(n):
            left_sum += nums[i]
            left_average[i] = left_sum//(i+1)
            
        for j in range(n-2,-1,-1):    
            right_sum += nums[j+1]
            right_average[j] = right_sum//(n-1-j)
            
            
        for i in range(n):
            avgAtIndex = abs(left_average[i] - right_average[i])
            if avgAtIndex < minAvgDiff:
                minAvgDiff = avgAtIndex
                index_result = i
                

        return index_result
        
        
        