class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)

        ans = [0] * (n + m)

        carry = 0

        startIndex = 0 # backwards

        for j in range(m - 1, -1, -1):
            index = startIndex
            for i in range(n - 1, -1, -1):
                calc = carry + ans[index] + (int(num2[j]) * int(num1[i]))

                carry = calc // 10
                ans[index] = calc % 10

                index += 1
            
            ans[index] = carry
            carry = 0
            
            startIndex += 1

        numAns = ''

        print(ans)

        ans.reverse()
    
        for element in ans:
            numAns += str(element)
                    
        numAns = numAns.lstrip('0')
                
        return numAns if numAns else '0'
