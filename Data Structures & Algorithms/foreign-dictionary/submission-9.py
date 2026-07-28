from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # the list is sorted already
        # make a graph
        # make sure no cycle, indegree 0 stuff

        # initial pass to make sure no later word contains prev word as a subset

        if len(words) == 1:
            return words[0]
        graph = {}
        indegrees = {}

        queue = deque()

        for i in range(1, len(words)):
            if len(words[i-1]) > len(words[i]):
                currWord = words[i-1]
                print(f"{currWord[:len(words[i])]} {words[i]}")
                if currWord[:len(words[i])] == words[i]:
                    return ""

            word1 = words[i-1]
            word2 = words[i]

            for char in word1:
                if char not in indegrees:
                    indegrees[char] = 0
                if char not in graph:
                    graph[char] = []

            for char in word2:
                if char not in indegrees:
                    indegrees[char] = 0
                if char not in graph:
                    graph[char] = []

            for j in range(len(word1)):
                if j == len(word2):
                    break

                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegrees[word2[j]] += 1
                    break
        
        ans = ""

        set1 = set(graph.keys())
 
        for key, value in indegrees.items():
            print(f"{key} {value}")
            if value == 0:
                queue.append(key)

        while queue:
            curr_char = queue.popleft()
            ans += curr_char
            print(ans)

            for char in graph[curr_char]:
                indegrees[char] -= 1
                if indegrees[char] == 0:
                    queue.append(char)
            
        #print(ans)

        if len(ans) != len(set1):
            return ""
            
        return ans

        
        

