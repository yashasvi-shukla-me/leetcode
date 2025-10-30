"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

#   Brute Force Approach ( O(n ^ 3)  TLE)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0

        for left in range(len(nums)):
            for right in range(left + 1, len(nums) + 1):
                if sum(nums[left:right]) == k:
                    c = c + 1
        return c


#   Improved Brute Force (TLE)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0

        for left in range(len(nums)):
            curr_sum = 0
            for right in range(left, len(nums)):
                curr_sum += nums[right]
                if curr_sum == k:
                    c += 1
        return c


#   Brute Force will result in TLE
#   we will use
#   HashMap + Prefix Sum

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        c = 0   # count of subarray whose sum is k
        prefixSum = 0
        hashMap = {0: 1}    # { prefixSumValue: frequency }

        for num in nums:

            prefixSum = prefixSum + num

            if (prefixSum - k) in hashMap:
                c = c + hashMap[prefixSum - k]

            hashMap[prefixSum] = hashMap.get(prefixSum, 0) + 1

        return c