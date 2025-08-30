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

#   Using Counter (Hash Map)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hash_map = Counter(nums)
        majority = []

        for num, freq in hash_map.items():
            if freq > len(nums) // 3:
                majority.append(num)
        return majority


#   Using Boyer-Moore Voting Algo

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count1 = count2 = 0
        candidate1 = candidate2 = None

        for num in nums:
            if num == candidate1:
                count1 = count1 + 1
            elif num == candidate2:
                count2 = count2 + 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 = count1 - 1
                count2 = count2 - 1

            # until this step, we find possible candidates
            # then we check whether actually they occur more than n//3 times

        majority = []
        for i in {candidate1, candidate2}: # for removing duplicates
            if nums.count(i) > len(nums) // 3:
                majority.append(i)
        return majority