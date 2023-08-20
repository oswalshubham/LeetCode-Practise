class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        '''
        x = 12

        0 1 2 3 4 5 6
              e
                s 

        '''
        start = 0
        end = x//2

        while start <= end:
            mid = start + (end-start)//2

            curr_square = mid*mid
            if curr_square == x:
                return mid
            
            elif curr_square < x:
                start = mid +1
            
            else:
                end = mid-1

        return end

        

