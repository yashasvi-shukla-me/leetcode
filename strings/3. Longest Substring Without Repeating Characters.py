"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

#   Brute Force Approach

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for i in range(len(s)):
            saw = set()

            for j in range(i, len(s)):
                if s[j] in saw:
                    break
                saw.add(s[j])
                longest = max(longest, j -i + 1)

        return longest


#   Sliding Window using HashSet

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        left = 0
        longest = 0

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left = left + 1
            window.add(s[right])
            longest = max(longest, right - left + 1)

        return longest