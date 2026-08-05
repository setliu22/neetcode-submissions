class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def solver(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours <= h

        bot = 1
        top = max(piles)

        while bot < top:
            middle = (bot + top) // 2

            if solver(middle):
                top = middle
            else:
                bot = middle + 1

        return bot