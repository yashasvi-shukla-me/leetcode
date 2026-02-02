"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""

# We can solve using sort(), sorted(), and others
# but to sort in-place, in one pass, we use
# Dutch National Flag (DNF) algo

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low = low + 1
                mid = mid + 1

            elif nums[mid] == 1:
                mid = mid + 1

            else: # when nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high = high - 1
