class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row first

        found = False
        bot = 0
        top = len(matrix)-1

        """
        0, 4 -> 2
        3, 4 -> 3

        """

        while not found and bot <= top:
            middle = (bot+top)//2

            if target < matrix[middle][0]:
                top = middle-1
            elif target > matrix[middle][-1]:
                bot = middle+1
            else:
                found = True
                row = middle
        
        if not found:
            return False
        
        print(row)

        found = False
        bot = 0
        top = len(matrix[0])-1

        while not found and bot <= top:
            middle = (bot + top) // 2

            if target < matrix[row][middle]:
                top = middle - 1
            elif target > matrix[row][middle]:
                bot = middle + 1
            else:
                return True

        return False

        # then find the column
