class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        left = 0
        right = len(nums) - 1
        i = (left+right)//2
        while left<=right:
            if nums[i] > target:
                right = i-1
            elif nums[i] < target:
                left = i+1
            elif nums[i] == target:
                return i
            i = (left+right)//2
        return -1
            
            