from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        
        ansList = []
        indegrees = [0] * numCourses
        courseList = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indegrees[a] += 1
            print(f"{a, b}")
            courseList[b].append(a)
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        processed = 0
        while queue:
            processed += 1
            
            curr = queue.popleft()
            ansList.append(curr)
            print(curr)
            for item in courseList[curr]:
                indegrees[item] -= 1
                if indegrees[item] == 0:
                    queue.append(item)
        print(processed)

        if processed != numCourses:
            return []
        else:
            return ansList
        

