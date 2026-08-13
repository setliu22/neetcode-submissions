class Solution:
    def reverseBits(self, n: int) -> int:
        twoPower = 31
        
        ans = 0

        while n != 0:
            if n & 1:
                ans += 2**twoPower

            n >>= 1

            twoPower -= 1

        return ans