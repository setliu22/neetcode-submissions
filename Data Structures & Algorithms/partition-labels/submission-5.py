class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # just find the repeat characters
        # find the last x. the characters contained within x cannot be a separate part
        # because y is trapped between the x's it must be included in the substring
        # then once we find another y anything trapped within must be looked at

        n = len(s)

        set1 = set()

        for char in s:
            set1.add(char)

        furthest = {}
        
        for char in set1:
            for i in range(n-1, -1, -1):
                if s[i] == char:
                    furthest[char] = i
                    break
            
        start = 0
        end = 0
        i = 0

        ans = []

        while i < n:
            end = max(end, furthest[s[i]])

            if i == end:
                ans.append(end-start+1)
                start = end+1

            i += 1
        
        return ans
        

