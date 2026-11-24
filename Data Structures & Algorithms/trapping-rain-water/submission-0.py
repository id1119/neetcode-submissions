class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        currentMaxI = 0
        currentMaxJ = 0
        i=0
        j= len(height)-1
        while i<=j:
            if currentMaxI<=currentMaxJ:
                if height[i]>currentMaxI:
                    currentMaxI = height[i]
                water += currentMaxI - height[i]
                i+=1
            else:
                if height[j]>currentMaxJ:
                    currentMaxJ = height[j]
                water+= currentMaxJ-height[j]
                j-=1
        return water 