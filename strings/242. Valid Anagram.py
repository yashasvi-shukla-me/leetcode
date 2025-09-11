"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

s and t consist of lowercase English letters.
"""

#   Brute Force

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# Using Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


#   Using HashMap

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for ch in s:
            s_count[ch] = s_count.get(ch, 0) + 1

        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1

        return s_count == t_count


#   Using Fixed Array (Optimal)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count = [0] * 26  # creates an array of 26 zeros

        for ch in s:
            count[ord(ch) - ord('a')] += 1  # increment that position in count

        for ch in t:
            count[ord(ch) - ord('a')] -= 1  # decrement that position in count

        return all(x == 0 for x in count) # checks if every value in count is 0