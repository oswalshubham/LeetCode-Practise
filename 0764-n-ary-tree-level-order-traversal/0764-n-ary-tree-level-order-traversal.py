"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = deque([root])
        result = []

        if root is None:
            return result

        while queue:
            curr_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_level.append(node.val)

                for child in node.children:
                    queue.append(child)

            result.append(curr_level)

        
        return result
