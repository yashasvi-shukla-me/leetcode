"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]
Output: false

Explanation:
All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

#   Using HashMap

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for i in nums:
            if i in hash_map:
                return True
            hash_map[i] = 0
        return False


#   Using Set
#   It's better to use set than dictionary, as we need only key and not value

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        stalker = set()

        for i in nums:
            if i in stalker:
                return True
            stalker.add(i)
        return False  


#   Simple but takes O(n) space

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(set(nums)) == len(nums):
            return False

        return True


#   To achieve constant space, time will increase O(n log n), space O(1)
#   Using sorting

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False