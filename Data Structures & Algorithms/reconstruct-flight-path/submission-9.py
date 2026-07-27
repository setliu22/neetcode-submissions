from collections import deque

import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        stack = ["JFK"]

        path = deque()

        graph = {}

        for origin, destination in tickets:
            if origin not in graph:
                graph[origin] = []
                heapq.heappush(graph[origin], destination)
            else:
                heapq.heappush(graph[origin], destination)
        
        while stack:
            print(f"{stack[-1]}")
            if stack[-1] in graph:
                print(f"{graph[stack[-1]]}")
            if stack[-1] not in graph or graph[stack[-1]] == []:
                curr_element = stack.pop()
                path.appendleft(curr_element)
            else:
                stack.append(heapq.heappop(graph[stack[-1]]))
 
        return list(path)