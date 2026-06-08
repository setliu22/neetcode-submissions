"""
The first solution was DFS coloring.

The newer solution is BFS using indegrees, also called Kahn’s algorithm.

They are two different ways to detect whether the course graph contains a cycle.

bfs is basically a simulator, # of times you process should = # of nodes

"""

from collections import deque
from typing import List

class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        if len(order) != numCourses:
            return []

        return order