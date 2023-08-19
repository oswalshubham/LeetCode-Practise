from collections import deque
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        todo = {}

        for i in range(numCourses):
            graph[i] = []
            todo[i] = []

        for a,b in prerequisites:
            graph[b].append(a)
            todo[a].append(b)

        queue = deque()

        for course,prereq in todo.items():
            if len(prereq) == 0:
                queue.append(course)

        '''
        [[1,4],[2,4],[3,1],[3,2]]
        graph = {1:[3], 2: [3], 3: [], 4:[1,2], 5:[]}
        todo = {}

        queue = []  
        currCourse = 3  

        '''

        while len(queue) > 0:
            currCourse = queue.popleft()

            for nextCourse in graph[currCourse]:
                todo[nextCourse].remove(currCourse)

                if len(todo[nextCourse]) == 0:
                    queue.append(nextCourse)

            todo.pop(currCourse)

        if len(todo) > 0:
            return False
        else:
            return True



        

        