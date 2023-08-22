import heapq

from collections import deque

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        mstset = set()

        min_distances = [float('inf')]*len(points)

        total_cost = 0
        queue = deque([(0,0)])

        while queue:
            curr_point,cost = queue.pop()
            total_cost+=cost
            for i in range(len(points)):
                if i!=curr_point and i not in mstset:
                    curr_distance = abs(points[curr_point][0]-points[i][0])+abs(points[curr_point][1]-points[i][1])
                    if curr_distance < min_distances[i]:
                        min_distances[i] = curr_distance

            mstset.add(curr_point)
            min_distances[curr_point] = float('inf')
            
            next_cost = min(min_distances)

            if next_cost!= float('inf'):
                queue.append((min_distances.index(next_cost),next_cost))


        return total_cost

            

        