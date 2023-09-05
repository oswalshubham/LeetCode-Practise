from collections import deque

class Solution:
    def reachNumber(self, target: int) -> int:
        sum = 0
        steps = 0

        target = abs(target)

        while sum < target:
            steps+=1
            sum+= steps  

        while (sum-target)%2 == 1:
            steps+=1
            sum+= steps
    
        return steps

        