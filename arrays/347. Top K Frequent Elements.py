"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
"""

#   Using Heap

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        heap = []   # initalized an empty heap


        for num, count in freq.items():
            heapq.heappush(heap, (count, num)) # pushes into heap (count, nums) 
            # smallest count at root

            if len(heap) > k:
                heapq.heappop(heap) # root is popped

        return [num for count, num in heap] # out of count, num we want num


#   Using Bucket Sort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        bucket = [[] for x in range(len(nums)+1)]
        for num, count in freq.items():

            bucket[count].append(num)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result