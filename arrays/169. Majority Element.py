"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

#   Brute Force

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        for num in nums:
            if nums.count(num) > len(nums)// 2:
                return num


#   Using Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        for num in count:
            if count[num] > len(nums) // 2:
                return num


#   Using Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Think of array as a voting process
        # Imagine the majority element as a candidate that gains +1 vote when encountered
        # Every different number cancels out one vote
        
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count = count + (1 if candidate == num else -1)

        return candidate