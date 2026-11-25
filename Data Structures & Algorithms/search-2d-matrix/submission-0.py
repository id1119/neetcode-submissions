class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            midH = (top+bottom) // 2
            if matrix[midH][0]<=target and matrix[midH][len(matrix[midH])-1]>= target:
                while left<=right:
                    midL = (left+right) // 2
                    if matrix[midH][midL]>target:
                        right = midL - 1
                    elif matrix[midH][midL]<target:
                        left = midL + 1
                    elif matrix[midH][midL]==target:
                        return True
                return False
            elif matrix[midH][0]>target:
                bottom = midH  -1
            elif matrix[midH][len(matrix[midH])-1]<target:
                top = midH + 1
        return False