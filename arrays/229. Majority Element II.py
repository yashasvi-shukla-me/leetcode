"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]
"""

#   Brute Force will result in TLE

#   Using Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        c = Counter(nums)
        majority = []
        n = len(nums)

        for i in c:
            if c[i] > n // 3:
                majority.append(i)

        return majority


#   Extended Boyer-Moore Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        candy1 = candy2 = None
        count1 = count2 = 0

        for num in nums:

            if num == candy1:
                count1 += 1
            elif num == candy2:
                count2 += 1
            elif count1 == 0:
                candy1 = num
                count1 += 1
            elif count2 == 0:
                candy2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        if nums.count(candy1) > len(nums) // 3:
            result.append(candy1)
        if nums.count(candy2) > len(nums) // 3:
            result.append(candy2)

        return result