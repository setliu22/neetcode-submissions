class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # identify at least 1 triplet for each value you want
        # you can't count triplets that have a value greater than the other values
        # any triplets that have a value greater than a target value are unusable
        # see if, after isolating usable triplets, you have all the target values you want

        goodIndices = []

        firstTrue = False
        secondTrue = False
        thirdTrue = False

        for i in range(len(triplets)):
            triplet = triplets[i]
            add = True
            for i in range(3):
                if triplet[i] > target[i]:
                    add = False
            
            if add:
                if triplet[0] == target[0]:
                    firstTrue = True
                if triplet[1] == target[1]:
                    secondTrue = True          
                if triplet[2] == target[2]:
                    thirdTrue = True

        return (firstTrue and secondTrue and thirdTrue)
            

