class Solution:
    def arrangeCoins(self, n: int) -> int:

        low = 1
        high = n


        while low<=high:
            mid = low + (high-low)//2

            coins_needed = mid*(mid+1)/2

            if coins_needed == n:
                return mid

            elif coins_needed > n:
                high = mid-1

            else:
                low = mid+1

        return high