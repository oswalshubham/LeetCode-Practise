class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        todo = {}
        result = []

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


        while len(queue) > 0:
            currCourse = queue.popleft()

            for nextCourse in graph[currCourse]:
                todo[nextCourse].remove(currCourse)

                if len(todo[nextCourse]) == 0:
                    queue.append(nextCourse)
            result.append(currCourse)
            todo.pop(currCourse)

        return result if len(todo) == 0 else []