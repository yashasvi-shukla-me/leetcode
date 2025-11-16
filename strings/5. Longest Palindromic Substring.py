"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
"""

#   Using Two Pointers

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(l, r):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1

            return s[l + 1 : r]

        longest = ""

        for i in range(len(s)):

            odd = expand(i, i)
            even = expand(i, i + 1)

            longest = max(longest, odd, even, key=len)

        return longest