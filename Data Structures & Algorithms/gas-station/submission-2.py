class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        results = [x-y for x, y in zip(gas, cost)]

        if sum(results) < 0:
            return -1

        print(results)

        max_index = 0

        max_gas = results[0]

        for i in range(1, len(results)):
            if results[i] > max_gas:
                max_index = i
                max_gas = max_index
        
        return max_index