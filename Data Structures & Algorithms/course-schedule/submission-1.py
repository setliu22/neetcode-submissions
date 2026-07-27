from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()

        # anything with indegree 0 goes to front of queue
        # return if processed all of the courses

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
            print(curr)
            for item in courseList[curr]:
                indegrees[item] -= 1
                if indegrees[item] == 0:
                    queue.append(item)
        print(processed)
        return processed == numCourses
        


