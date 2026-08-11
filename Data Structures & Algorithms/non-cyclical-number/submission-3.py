class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(num):
            ans = 0
            num = str(num)
            for char in num:
                ans += ((int(char))**2)
            return ans

        set1 = set()

        while n != 1:
            n = helper(n)
            if n in set1:
                return False
            set1.add(n)
                    
        if n == 1:
            return True
