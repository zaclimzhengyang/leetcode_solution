# https://leetcode.com/problems/contains-duplicate/
# using set method

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicateSet = set()

        for num in nums:
            if num in duplicateSet:
                return True
            else:
                duplicateSet.add(num)
        return False
