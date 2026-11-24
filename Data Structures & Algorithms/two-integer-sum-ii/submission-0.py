class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dict = {}
        for i in range(len(numbers)):
            remainder = target - numbers[i]
            if remainder in dict and dict[remainder] < i:
                return [dict[remainder]+1, i+1]
            dict[numbers[i]] = i