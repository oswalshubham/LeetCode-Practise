"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        dic = {}
        
        dic[node.val] = Node(node.val)
        
        queue = deque([])
        
        queue.appendleft(node)
        
        while len(queue) > 0 :
            tempNode = queue.pop()

            for neighb in tempNode.neighbors:
                if neighb.val not in dic:
                    dic[neighb.val] = Node(neighb.val)
                    queue.appendleft(neighb)
                    
                dic[tempNode.val].neighbors.append(dic[neighb.val])
                
        
        return dic[1]
                
                
                
        
        