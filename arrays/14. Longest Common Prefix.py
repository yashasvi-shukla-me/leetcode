"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

# #   Sorting

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()  # works due to lexicographic sorting
        first, last = strs[0], strs[-1]
        prefix = ""

        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                prefix = prefix + first[i]
            else:
                break
        return prefix