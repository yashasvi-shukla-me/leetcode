"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
"""

#   Merge Sort (Optimal)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr):

            if len(arr) <= 1: # already sorted, as it has 0 or 1 element
                return arr

            mid = len(arr) // 2

            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        def merge(left, right):

            i = j = 0
            merged = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i = i + 1
                else:
                    merged.append(right[j])
                    j = j + 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged

        return mergeSort(nums)
    
#   Counting Sort is faster
#   applicable only because we have a constraint in this problem