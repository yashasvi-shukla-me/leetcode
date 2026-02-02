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

#   Using Sliding Window + HashMap

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if k ==0 or not s:
            return 0

        left = 0
        n = len(s)
        freq = {}
        maxLen = 0

        for right in range(n):

            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen


#   Sliding Window + defaultdict

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        left = 0
        n = len(s)
        freq = defaultdict(int)
        maxLen = 0

        for right in range(n):

            freq[s[right]] += 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen