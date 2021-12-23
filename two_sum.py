# https://leetcode.com/problems/two-sum/

"""
sort the list of nums
create an empty result list
loop through index,value in enumerate nums
check that at a particular index > 0, the value is equal to the value at the previous index, we want to skip it using continue
assign left pointer to index + 1, to the right of index
assign right pointer to len(nums) - 1, the very end of the nums list
while left pointer is smaller than right pointer, threesum = value + nums at left pointer + nums at right pointer
if three sum > 0, shift the right pointer to the left, -1
if three sum < 0, shift the left pointer to the right, +1
if three sum = 0, append the three numbers to the result list
then shift the left pointer to the right, +1
in the case the new value at left pointer is also the same number as previous,
shift the left pointer to the right,+1. keeping in mind left pointer < right pointer
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numslist = []
        for index, value in enumerate(nums):
            numslist.append([value,index])
        numslist = sorted(numslist)
        left = 0
        right = len(nums) - 1
        while left <= right:
            if numslist[left][0] + numslist[right][0] < target:
                left += 1
            elif numslist[left][0] + numslist[right][0] > target:
                right -= 1
            else:
                return [numslist[left][1], numslist[right][1]]