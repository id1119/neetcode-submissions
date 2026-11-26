class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        counter = 0
        if len(nums) == 1:
            return nums[0]
        while left<right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]
