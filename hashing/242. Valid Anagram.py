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

#   We can solve using Counter and sorted (takes O(n) space)
#   Using HashMap 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sCount = {}
        tCount = {}

        for ch in s:
            sCount[ch] = sCount.get(ch, 0) + 1
        for ch in t:
            tCount[ch] = tCount.get(ch, 0) + 1
        
        return sCount == tCount


#   Using Optimized HashMap
#   as given s and t consist of lowercase English letters

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        arr = [0] * 26

        for ch in s:
            arr[ord(ch) - ord('a')] += 1

        for ch in t:
            arr[ord(ch) - ord('a')] -= 1

        return all(x == 0 for x in arr)