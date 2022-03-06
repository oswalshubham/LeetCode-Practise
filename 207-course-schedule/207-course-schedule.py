from collections import deque
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        todo = {i: set() for i in range(numCourses)} 
        graph = defaultdict(set)
            
        for i,j in prerequisites:
            todo[i].add(j)
            graph[j].add(i)
            
        queue = deque([])
            
        for key,value in todo.items():
            if len(value) == 0:
                queue.appendleft(key)
                
        while queue:
            k = queue.pop()
            
            for i in graph[k]:
                todo[i].remove(k)
                if len(todo[i])==0:
                    queue.appendleft(i)
                    
            todo.pop(k)
            
        return not todo
                        
        
        
        