class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []
        
        n = len(s)

        def is_palindrome(strng):
            left = 0
            right = len(strng)-1
            while left < right:
                if strng[left] != strng[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True

        def dfs(index, lst):
            print(f"{lst} {index}")
            if index == n:
                ans.append(lst[:])
                return

            # all possible string lengths from index to the end

            for end in range(index, n):
                if is_palindrome(s[index:end+1]):
                    lst.append(s[index:end+1])
                    dfs(end+1, lst)
                    lst.pop()

        dfs(0, [])

        return ans

        

