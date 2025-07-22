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


#   Optimal Approach (Prefix Sum, Hash Map)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0   # maintaining count of subarrays whose sum = k
        prefix_sum = 0
        prefix_count = {0: 1}   # keeping the count of each prefix_sum {prefix_sum : count}

        for num in nums:
            prefix_sum = prefix_sum + num

            if (prefix_sum - k) in prefix_count:
                count = count + prefix_count[prefix_sum - k]
            
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count