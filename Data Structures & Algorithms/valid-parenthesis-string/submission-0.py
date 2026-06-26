"""
do a left-ro-right and right-to-left scan

Check 1: No ) can appear without something before it

Scan left to right. Treat * as ( when needed.

"(*))"

(  gives us 1 possible opening
*  gives us another possible opening
)  uses one
)  uses one

If the count ever goes below 0, there are too many ).

Check 2: No ( can remain without something after it

Scan right to left. Treat * as ) when needed.

If the count ever goes below 0, there are too many (.

too many ( or )

* we can just treat as nothing if surplus

too much either way
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0