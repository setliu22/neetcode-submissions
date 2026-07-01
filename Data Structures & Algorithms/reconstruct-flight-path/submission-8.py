""" 
it's going to be cycles and a potential single final dead end
if no dead end it's just one big cycle
always do lexo smallest first

1. Explicit insertion

You:

Build a path until stuck.
Find an airport in that path with unused tickets.
Build another path from there.
Insert the new path into the original path.
Repeat.

Example:

Initial path: A → B
Extra path from A: A → E → C → D → A

Insert at A:

A → E → C → D → A → B

2. Recursion or stack

You follow tickets until stuck, then add airports to the answer while backtracking.

def visit(airport):
    while tickets_from_airport_exist:
        next_airport = smallest_unused_ticket()
        visit(next_airport)

    route.append(airport)

Then reverse route.

The recursion automatically puts later-discovered paths in the correct position, so you never explicitly perform an insertion.

The recursion’s entire point is that it avoids manually inserting:

A → E → C → D → A

before:

A → B

Appending during backtracking automatically creates the route in reverse insertion order. Then one final reverse gives the correct itinerary.

Or:

route.appendleft(airport) (append left is like reversing)

This places each airport at the front, so no final reverse is needed.

only do not record a letter if it has other paths still need to be explored

then when you reach A again after cycling record it and everything before it

insert the A -> A thing reversed

Then reverse the whole thing
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