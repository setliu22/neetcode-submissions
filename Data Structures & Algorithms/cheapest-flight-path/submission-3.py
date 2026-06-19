"""
Dijkstra-style approach:

Use a min-heap:

(cost_so_far, airport, flights_used)

When you pop the cheapest state:

if airport == dst, return cost_so_far
if flights_used <= k, try taking another flight
do not expand beyond k + 1 flights

This works because all prices are nonnegative.

Bellman-Ford approach:

at most 1 flight
[0, 100, 500]

next round is at most 2 flights
[0, 100, 200]

Use a copy to avoid a round adding more than one flight
Read from old prices, write updates into a temp copy
temp = prices[:]

So suppose this gets popped:

(cost=200, airport=dst, flights_used=2)

That means every other route currently in the heap costs at least 200.

Because all flight prices are nonnegative, any future route made by adding more flights will only get more expensive, not cheaper.

So once dst is popped, you can safely return.
"""

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = float("inf")

        prices = [INF] * n
        prices[src] = 0

        # k stops means at most k + 1 flights
        for _ in range(k + 1):
            temp = prices[:]

            for from_airport, to_airport, price in flights:
                if prices[from_airport] != INF:
                    new_price = prices[from_airport] + price
                    temp[to_airport] = min(temp[to_airport], new_price)

            prices = temp

        return -1 if prices[dst] == INF else prices[dst]