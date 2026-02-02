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

#   Brute Force Approach
#   Using Counter + Sorting

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        sortedElements = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        topK = [element for element, count in sortedElements[:k]]

        return topK


#   Using Heap
#   Time Complexity: O(N log K), Space Complexity: O(N)

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        minHeap = []

        for num, count in freq.items():
            heapq.heappush(minHeap, (count, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [num for count, num in minHeap]
    
#   Using Bucket Sort
#   Time Complexity: O(N), Space Complexity: O(N)