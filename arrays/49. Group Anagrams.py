"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

#   Using Sorting and HashMap

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())


#   Using Character Count and HashMap

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26
            
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)  # as list is unhashable
                                # all anagrams produce same tuple

            groups[key].append(word)

        return list(groups.values())