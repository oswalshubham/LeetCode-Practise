from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for source, dest, cost in flights:
            graph[source].append([dest,cost])
        
        costMap = {src:0}

        queue = deque([(src, 0, 0)])

        while queue:
            city, curr_cost, stops = queue.popleft()
            if stops <= k:
                for next_city, cost in graph[city]:
                    if next_city not in costMap or curr_cost+cost < costMap[next_city]:
                        costMap[next_city] = curr_cost+cost  
                        queue.append((next_city, costMap[next_city],stops+1))

        return costMap[dst] if dst in costMap else -1

        '''
        
        costMap = {0:0, 1:100, 2:200, 3:700}

        return costMap[dst]
        '''

        
        

        