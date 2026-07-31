class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0
        n = len(gas)

        for i in range(n):
            difference = gas[i] - cost[i]

            total += difference
            tank += difference

            if tank < 0:
                start = i+1
                print(start)
                tank = 0
        
        return start if total > -1 else -1 
            
        

