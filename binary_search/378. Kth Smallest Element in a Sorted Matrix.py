"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
"""

# Using Heaps
# but it is not optimal

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap = [] # heap is a list
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                heapq.heappush(heap, matrix[i][j])

        for _ in range(k-1):
            heapq.heappop(heap)

        return heap[0]


# Improved Heap, still not Optimal

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap = [] # heap is a list
        n = len(matrix)

        for r in range(n):
            heapq.heappush(heap, (matrix[r][0], r, 0))

        for _ in range(k):
            val, r, c = heapq.heappop(heap)

            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

        return val


# Optimal method
# Using Binary Search

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]

        def count_less_equal(mid):
            count = 0
            row = 0
            col = n - 1

            while row < n and col >= 0:
                if matrix[row][col] <= mid:
                    count = count + col + 1
                    row = row + 1
                else:
                    col = col - 1

            return count

        while low < high:
            mid = (low + high) // 2

            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid 

        return low # or high