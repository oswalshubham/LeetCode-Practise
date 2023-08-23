from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        [1,5,6,7,8,10,6,5,6]  max = 5
             l          r
        minQ = [4,7]
        maxQ = [7]
        
        '''

        minQ = deque([])
        maxQ = deque([])

        left = 0
        max_count = 0

        for right in range(len(nums)):
            
            while minQ and minQ[-1]>nums[right]:
                minQ.pop()

            
            while maxQ and maxQ[-1]<nums[right]:
                maxQ.pop()

            minQ.append(nums[right])
            maxQ.append(nums[right])

            while maxQ[0] - minQ[0] > limit:
                if nums[left] == minQ[0]:
                    minQ.popleft()

                if nums[left] == maxQ[0]:
                    maxQ.popleft()

                left+=1

            max_count = max(max_count, right-left+1)
        
        return max_count



            




        

        

