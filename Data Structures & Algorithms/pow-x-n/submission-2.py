class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        even exponent:
        x^n = x^(n/2) * x^(n/2)

        odd exponent:
        x^n = x * x^(n-1)
        """

        flip = False

        if n < 0:
            n = -n
            flip = True

        ans = 1

        while n > 0:
            if n % 2 != 0:
                ans *= x

            x *= x
            
            n = n // 2

        if flip:
            return 1 / ans
        else:
            return ans
