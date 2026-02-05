"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true

Example 5:

Input: s = "([)]"
Output: false
"""

#   Simple solution using string replacement

class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)//2):

            s = s.replace("{}", "").replace("[]", "").replace("()", "")

        if len(s) == 0:
            return True
        return False
    

#   Using stack data structure

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        match = {
            ")": "(",
            "]":"[",
            "}":"{"
        }

        for ch in s:
            if ch not in match:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != match[ch]:
                    return False
                stack.pop()

        return not stack # return True if stack is empty i.e. string was valid