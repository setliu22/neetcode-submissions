import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        heap = [(0, k)]

        graph = [[] for _ in range(n+1)]

        visited = set()

        ans = 0

        for source, target, time in times:
            graph[source].append((target, time))

        while heap:
            if len(visited) == n:
                break

            curr_dist, curr_node = heapq.heappop(heap)

            ans = curr_dist

            if curr_node in visited:
                continue

            visited.add(curr_node)

            for target, time in graph[curr_node]:
                print(target)
                if target not in visited:
                    heapq.heappush(heap, (curr_dist+time, target))
        
        return ans if len(visited) == n else -1

