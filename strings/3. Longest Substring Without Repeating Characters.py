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

#   Brute Force Approach ( O(N^2) )

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                maximum = max(maximum, j - i + 1)
        return maximum


#   Sliding Window + HashSet

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maximum = 0
        window = set()

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left = left + 1
            window.add(s[right])
            maximum = max(maximum, right - left + 1)
            
        return maximum


#   Sliding Window + HashMap

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maximum = 0
        seen_last = {}  # like {a : 0}

        for right in range(len(s)):
            if s[right] in seen_last and seen_last[s[right]] >= left:
                left = seen_last[s[right]] + 1
            seen_last[s[right]] = right
            maximum = max(maximum, right - left + 1)
            
        return maximum