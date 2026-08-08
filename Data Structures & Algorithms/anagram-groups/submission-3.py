class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict1 = {}

        for word in strs:
            counter = tuple(sorted(word))
            #print(counter)
            if counter not in dict1:
                dict1[counter] = [word]
            else:
                dict1[counter].append(word)
        
        ans = [dict1[counter] for counter in dict1]

        return ans