"""
Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.

Constraints:
0 <= s.length <= 10^5
0 <= k <= 26

Example 1:
Input:
s = "eceba", k = 2
Output:
3

Explanation:
The longest substring with at most 2 distinct characters is "ece".

Example 2:
Input:
s = "aa", k = 1
Output:
2

Explanation:
The longest substring with at most 1 distinct character is "aa".

Follow-up:
Can you solve this in O(n) time?
"""

#   Using Sliding Window

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:    # if string is empty or k = 0, return 0
            return 0

        left = 0
        longest = 0
        freq = {}

        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]   # if the freq becomes zero, remove that element
                left += 1

            longest = max(longest, right - left + 1)

        return longest