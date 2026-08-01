class Solution:
    def checkValidString(self, s: str) -> bool:
        unclosed = []
        safety = []

        for i, char in enumerate(s):
            if char == '(':
                unclosed.append(i)

            elif char == '*':
                safety.append(i)

            else:  # ')'
                if unclosed:
                    unclosed.pop()
                elif safety:
                    safety.pop()
                else:
                    return False

        # Remaining '(' must be closed by '*' appearing after them
        while unclosed and safety:
            if safety[-1] < unclosed[-1]:
                return False

            unclosed.pop()
            safety.pop()

        return not unclosed