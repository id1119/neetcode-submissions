class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            stackI = float('inf')
            while stack and h<stack[-1][1]:
                stackI, stackH = stack.pop()
                area = stackH * (i-stackI)
                if area > maxArea:
                    maxArea = area
                # print(stackH, stackI, area, maxArea)
            if stackI<i:
                stack.append([stackI,h])
            else:
                stack.append([i,h])
        if stack:
            for el in stack:
                area = el[1] * (len(heights)-el[0])
                if area > maxArea:
                    maxArea = area
        return maxArea