class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sortedList = []
        if target not in nums:
            return -1
        if len(nums) == 1:
            return 0
        for index, value in enumerate(nums):
            sortedList.append([value, index])
            sortedList = sorted(sortedList)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if sortedList[mid][0] > target:
                right = mid
            elif sortedList[mid][0] < target:
                left = mid + 1
            else:
                return sortedList[mid][1]