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


#   Using Min Heap

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heap[0]
    

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