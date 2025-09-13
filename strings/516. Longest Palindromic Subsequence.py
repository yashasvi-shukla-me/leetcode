"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""

# #   Using Recursion ( TLE )

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def lps(s, i, j):  # lps is not my school

            if i > j:
                return 0
            if i == j:
                return 1

            if s[i] == s[j]:
                return 2 + lps(s, i + 1, j -1)
            else:
                return max(lps(s, i+1, j), lps(s, i, j-1))

        return lps(s, 0, len(s)-1)


#   Using Memoization ( Recursion + Cache )
#   Dynamic Programming - Top Down

from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @lru_cache(None)
        def lps(i: int, j: int) -> int:

            if i > j :
                return 0
            if i == j:
                return 1

            if s[i] == s[j]:
                return 2 + lps(i + 1, j -1)
            else:
                return max(lps(i + 1, j), lps(i, j - 1))

        return lps(0, len(s) - 1)