"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

#   Using HashMap

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashMap = {}

        for i in range(len(nums)):
            if nums[i] in hashMap and i - hashMap[nums[i]] <= k:
                return True
            hashMap[nums[i]] = i

        return False


#   Sliding Window 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()

        for i in range(len(nums)):

            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])

        return False