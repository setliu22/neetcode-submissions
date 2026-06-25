"""

At the end:
If the total balance is negative, completing the circle is impossible.

Track two things:
total_gas  # gas balance across the entire route
tank       # gas balance from the current candidate start

If tank becomes negative at station i, the current starting station cannot work.

More importantly, no station between the current start and i can work either, because those stations would start with even less accumulated gas.

Therefore, try the next station:

start = i + 1
tank = 0

At the end:

If the total balance is negative, completing the circle is impossible.
Otherwise, start is the valid starting index.

The reset logic only proves:

“If a solution exists, this is the candidate.”

It does not prove that a solution exists.

remember there is only one answer so we should look for a candidate but still check out work

you can check in beginning or during loop

The common version tracks total_gas inside the same loop only to avoid a separate pass:

total_gas += gas[i] - cost[i]
"""

class Solution:
    def canCompleteCircuit(
        self,
        gas: List[int],
        cost: List[int]
    ) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start