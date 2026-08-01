class Solution:
    def checkValidString(self, s: str) -> bool:
        openIndices = []
        freeIndices = []

        for i in range(len(s)):
            if s[i] == '(':
                openIndices.append(i)
            elif s[i] == '*':
                freeIndices.append(i)
            else: # )
                # close the LATEST open index
                if openIndices:
                    openIndices.pop()
                elif freeIndices:
                    freeIndices.pop()
                else:
                    return False
            
        # *( is false

        while openIndices and freeIndices:
            if openIndices[-1] > freeIndices[-1]:
                return False

            openIndices.pop()
            freeIndices.pop()
        
        return openIndices == []




