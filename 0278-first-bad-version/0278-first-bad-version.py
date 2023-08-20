# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return n

        low = 1
        high = n


        while low < high:
            mid = low+(high-low)//2

            if isBadVersion(mid):
                high = mid

            else:
                low = mid+1

        return low               

        
