"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""

#   Using Set

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        unique = sorted(set(nums), reverse=True)

        if len(unique) >= 3:
            return unique[2]
        return unique[0]


#   Optimal using Three Trackers 
#   It's In-Place and takes O(1) space

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')

        for num in nums:
            if num in (first, second, third):
                continue    # skip if it exists

            if num > first:
                third, second, first = second, first, num   # just swapping
            elif num > second:
                third, second = second, num
            elif num > third:
                third = num

        return third if third != float('-inf') else first
        #   in this we check if the len(nums) <= 2, if yes then we return the max i.e first