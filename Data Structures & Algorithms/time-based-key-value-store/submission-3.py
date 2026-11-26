class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = []
        self.dictionary[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""

        left = 0
        right = len(self.dictionary[key]) - 1
        currentMax = -1
        currentMinIndex = 0

        while left <= right:
            mid = (left + right) // 2

            if self.dictionary[key][mid][1] <= timestamp and self.dictionary[key][mid][1] >= currentMax:
                currentMax = self.dictionary[key][mid][1]
                currentMinIndex = mid

            if self.dictionary[key][mid][1] == timestamp:
                return self.dictionary[key][mid][0]
            elif self.dictionary[key][mid][1] > timestamp:
                right = mid - 1
            elif self.dictionary[key][mid][1] < timestamp:
                left = mid + 1

        if currentMax == -1:
            return ""

        return self.dictionary[key][currentMinIndex][0]