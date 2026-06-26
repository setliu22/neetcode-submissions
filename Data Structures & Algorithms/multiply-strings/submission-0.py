"""
2 × 4 = 8  → [0, 0, 0, 8]
2 × 3 = 6  → [0, 0, 6, 8]
1 × 4 = 4  → [0, 0, 10, 8]
1 × 3 = 3  → [0, 3, 10, 8]
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Add every digit multiplication into its correct position
        for i in range(m - 1, -1, -1):
            digit1 = ord(num1[i]) - ord("0")

            for j in range(n - 1, -1, -1):
                digit2 = ord(num2[j]) - ord("0")
                result[i + j + 1] += digit1 * digit2

        # Move carries from right to left
        for i in range(m + n - 1, 0, -1):
            result[i - 1] += result[i] // 10
            result[i] %= 10

        # Remove the unused leading zero
        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1

        return "".join(str(digit) for digit in result[start:])