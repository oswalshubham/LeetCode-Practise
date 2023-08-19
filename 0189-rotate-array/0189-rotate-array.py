class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        '''while k > 0:

            for j in range(n-2,-1,-1):
                nums[j],nums[j+1] = nums[j+1],nums[j]

            k-=1'''

        nums[:] = nums[n-k:]+nums[:n-k]

        