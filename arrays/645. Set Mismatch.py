"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:

Input: nums = [1,1]
Output: [1,2]
"""

#   Using Set & Sum difference

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        # length of nums 
        n = len(nums)

        hashSet = set()

        for i in range(n):
            if nums[i] not in hashSet:
                hashSet.add(nums[i])
            else:
                dup = nums[i]

        sumOfN = (n * (n + 1)) // 2
        missing_num = sumOfN - sum(hashSet)

        return [dup, missing_num]


#   Using Index Marking

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        missing = -1
        dup = -1

        for num in nums:

            index = abs(num) - 1

            if nums[index] < 0:
                dup = abs(num)
            else:
                nums[index] = -nums[index]
                # marking the element at corrsponding index negative

        for i in range(len(nums)):
            if nums[i] > 0: # remained positive, never seen
                missing = i + 1

        return [dup, missing]