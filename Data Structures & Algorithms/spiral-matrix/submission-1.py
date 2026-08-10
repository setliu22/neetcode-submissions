class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        furthestUp = 1
        furthestRight = n - 1
        furthestDown = m - 1
        furthestLeft = 0

        i = 0
        j = 0

        output = []
        length = 0

        while length < n * m:            
            while j <= furthestRight:
                output.append(matrix[i][j])
                length += 1
                j += 1

            if length ==  n * m:
                break
            
            j -= 1

            furthestRight -= 1

            i += 1
        
            while i <= furthestDown:
                output.append(matrix[i][j])
                length += 1
                i += 1

            if length ==  n * m:
                break
            
            i -= 1

            furthestDown -= 1

            j -= 1

            while j >= furthestLeft:
                output.append(matrix[i][j])
                length += 1
                j -= 1

            if length ==  n * m:
                break
            
            j += 1

            furthestLeft += 1

            i -= 1

            while i >= furthestUp:
                output.append(matrix[i][j])
                length += 1
                i -= 1

            if length ==  n * m:
                break
            
            i += 1
            
            furthestUp += 1

            j += 1
        
        return output