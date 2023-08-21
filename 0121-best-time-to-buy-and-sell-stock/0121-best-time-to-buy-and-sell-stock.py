class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        

        profit = 0

        min_price = nums[0]

        for i in range(len(nums)):
            profit = max(profit, nums[i]-min_price)

            min_price = min(min_price, nums[i])

        return profit