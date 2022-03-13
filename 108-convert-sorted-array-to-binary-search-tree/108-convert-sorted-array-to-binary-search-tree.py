# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(low, high):
            if high < low or low>high:
                return None
            if low == high:
                return TreeNode(nums[low])
            if low<high:
                mid = low + (high-low)//2

                node = TreeNode(nums[mid])

                node.left = helper(low,mid-1)
                node.right = helper(mid+1,high)
                
            return node
        
        return helper(0,len(nums)-1)
            