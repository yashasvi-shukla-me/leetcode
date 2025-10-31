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

#   Using Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        c = Counter(nums)   # {num : frequency}

        for num in c:

            if c[num] > len(nums) // 2:
                return num


#   Boyer-Moore Algorithm
#   O(n) time and O(1) space

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        c = 0   # maintaining count
        candy = None    # storing majority element

        for num in nums:

            if c == 0:
                candy = num
            
            if candy == num:
                c = c + 1
            else:
                c = c - 1

        return candy