# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        preo_index = 0
        for index,value in enumerate(inorder):
            inorder_map[value] = index
            
        def constructTree(left,right):
            nonlocal preo_index
            
            if left>right:
                return None
            
            node_val = preorder[preo_index]
            root = TreeNode(node_val)
            
            preo_index+=1
            
            root.left = constructTree(left, inorder_map[node_val]-1)
            root.right = constructTree(inorder_map[node_val]+1,right)
            
            return root
            
            
            
        return constructTree(0,len(inorder)-1)