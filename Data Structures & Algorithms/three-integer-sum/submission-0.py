class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []
        seen = set()
        for i in range(len(nums)):
            if nums[i] >0:
                break
            s = set()
            for j in range(i+1, len(nums)):
                remainder = -(nums[i]+nums[j])
                if remainder in s:
                    triplet = tuple(sorted([nums[i], nums[j], remainder]))
                    if triplet not in seen:
                        seen.add(triplet)
                        output.append(list(triplet))
                s.add(nums[j])

        return output