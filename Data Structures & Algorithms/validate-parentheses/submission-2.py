from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()
        for item in s:
            if item in "([{":
                d.append(item)
            elif item == ")":
                a = d.pop() if d else 'a'
                if a != "(":
                    return False
            elif item == "]":
                a = d.pop() if d else 'a'
                if a != "[":
                    return False
            elif item == "}":
                a = d.pop() if d else 'a'
                if a != "{":
                    return False               
        return not d
