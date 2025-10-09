"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
"""

#   Backtracking approach
#   open is a built in function in python
#   had to use open_count

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(path, open_count, close_count):

            if len(path) == n * 2:
                res.append(path)
                return

            # adding '('
            if open_count < n:
                backtrack(path + '(', open_count + 1, close_count)

            # adding ')'
            if close_count < open_count:
                backtrack(path + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return res