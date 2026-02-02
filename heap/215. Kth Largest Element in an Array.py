"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

#   Brute Force approach

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort(reverse = True)
        return nums[k-1]


# Using sorting is very easy, but we have to solve without sorting
# Using Heaps

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:

            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]



# Using QuickSelect
# we won't need sorting
# Complexity O(n)

# it is faster in theory but may give TLE in python as it uses different partitioning scheme

import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        target = len(nums) - k # index of where our kth largest will occur

        def quickselect(left, right):

            if left == right:
                return nums[right]

            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]

            # move the pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left

            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index = store_index + 1

            nums[store_index], nums[right] = nums[right], nums[store_index]

            if store_index == target:
                return nums[target]

            elif store_index < target:
                return quickselect(store_index + 1, right)

            else:
                return quickselect(left, store_index - 1)

        return quickselect(0, len(nums) - 1)


#   Using Quickselect (Optimal)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k = len(nums) - k

        def quickselect(l, r):

            pivot = nums[random.randint(l, r)]
            left, right = l, r

            while left <= right:

                while nums[left] < pivot:
                    left = left + 1
                while nums[right] > pivot:
                    right = right - 1

                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left = left + 1
                    right = right - 1

            if k <= right:
                return quickselect(l, right)
            elif k >= left:
                return quickselect(left, r)
            else:
                return nums[k]

        return quickselect(0, len(nums) - 1)