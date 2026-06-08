from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        # [course, prereq] means prereq -> course
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 0 = unvisited
        # 1 = currently exploring
        # 2 = fully processed
        state = [0] * numCourses

        def dfs(course: int) -> bool:
            if state[course] == 1:
                return False  # cycle found

            if state[course] == 2:
                return True  # already checked successfully

            state[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False

        return True