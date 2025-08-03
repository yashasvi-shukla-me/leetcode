"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba")

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

#   Sliding Window + Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        left = 0
        s1_count = Counter(s1)
        window = Counter()

        for right in range(len(s2)):
            window[s2[right]] = window[s2[right]] + 1

            if right - left + 1 > len(s1):
                window[s2[left]] = window[s2[left]] - 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left = left + 1

            if window == s1_count:
                return True

        return False
    
#   Another faster method is available using Fixed Sized Array