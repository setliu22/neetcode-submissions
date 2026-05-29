class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, open_count, close_count):
            # If the string has n opening and n closing parentheses, it is complete
            if open_count == n and close_count == n:
                res.append(curr)
                return

            # Add '(' if we still have opening parentheses left
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Add ')' only if it would not exceed the number of '(' used
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res