"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

#   Brute Force using Bitmasking

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        
        for mask in range(1 << n):  
            subset = []

            for j in range(n):
                if mask & (1 << j):
                    subset.append(nums[j])
            res.append(subset)
        
        return res
    
    
#   Using Backtracking

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset[:])
                return 

            # to imclude the element
            subset.append(nums[i])
            backtrack(i + 1)

            # NOT include the element
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res