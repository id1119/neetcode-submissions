class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = sum(piles)//h
        if left == 0:
            left = 1
        right = max(piles)
        currentBest = float('inf')
        while left<=right:
            k = (left+right) // 2
            hours = 0
            for p in piles:
                if p<=k:
                    hours+=1
                elif p%k != 0:
                    hours+=(p//k)+1
                else:
                    hours += p/k
            if hours == h:
                if k<currentBest:
                    currentBest = k
                right = k - 1
            elif hours < h:
                if k<currentBest:
                    currentBest = k
                right = k - 1
            elif hours > h:
                left = k+1      
        return currentBest              

