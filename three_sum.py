# https://leetcode.com/problems/3sum/
nums = [4, 7, 12, 14, 5, 3, 4, 0, 0, -1, -4, -6, -3, -8, -9, -12, -14, -20, -13]

nums.sort()
result = []
for i in range(0, len(nums) - 2):
    if (i > 0 and nums[i] == nums[i - 1]):
        continue
    left = i + 1
    right = len(nums) - 1
    while left < right:
        total_sum = nums[i] + nums[left] + nums[right]
        if total_sum > 0:
            right -= 1
        elif total_sum < 0:
            left += 1
        else:
            result.append([nums[i], nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
print(result)
