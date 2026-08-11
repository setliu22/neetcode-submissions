class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        tenFactor = 1
        ans = 0

        # make num1 the longer one

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        one = 0

        for i in range(len(num1) - 1, -1, -1):
            one += tenFactor * int(num1[i])
            tenFactor *= 10
        
        print(one)

        tenFactor = 1

        ans = 0

        for i in range(len(num2) - 1, -1, -1):
            ans += tenFactor * int(num2[i]) * one
            tenFactor *= 10

        return str(ans)