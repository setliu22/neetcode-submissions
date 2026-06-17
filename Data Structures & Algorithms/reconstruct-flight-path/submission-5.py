""" since the data guaranteed to work, There is only one true final dead end in the completed itinerary, meaning the final airport of the whole route.

Keep taking the smallest unused ticket until stuck, then add that airport to the route, backtrack, and reverse the route at the end.

if its ABACA is will only see a dead end at the last A so everthing gets added correctly

in actuality even tho its one dead end that dead end is always the end of the path

either added naturally like a to z or if a to aaaa it is intentionally added last
"""

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)

                # Backtracking happens after dfs(next_airport) returns here

            route.append(airport)

        dfs("JFK")
        return route[::-1]