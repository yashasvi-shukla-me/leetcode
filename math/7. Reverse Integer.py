"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21
 
Constraints:
-231 <= x <= 231 - 1
"""

# Using string based reverse [::-1]

class Solution:
    def reverse(self, x: int) -> int:


        MIN = -(2 ** 31)
        MAX = 2 ** 31 - 1

        if x < 0:
            s = str(-x)[::-1]
            val = -int(s)
        
        else:
            s = str(x)[::-1]
            val = int(s)

        if MIN <= val <= MAX:
            return val
        else:
            return 0


# Without string based reverse [::-1]

class Solution:
    def reverse(self, x: int) -> int:


        MIN = -(2 ** 31)
        MAX = 2 ** 31 - 1

        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x!= 0:

            digit = x % 10 
            x = x // 10

            if rev > (MAX - digit) // 10: # imp, also no need to check against MIN
                return 0

            rev = rev * 10 + digit

        return sign * rev