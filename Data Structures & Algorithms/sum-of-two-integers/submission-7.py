class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        carry = 0

        while b:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask # sum without carry
            b = carry

        if a <= max_int:
            return a
        else:
            return -((~a & mask) + 1)
