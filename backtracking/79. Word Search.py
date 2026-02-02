"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

#   Backtracking & DFS

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, columns = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= rows or c >= columns or word[i] != board[r][c] or (r, c) in path:
                return False

            path.add((r, c))    # track

            res = (
                dfs(r + 1, c, i + 1) or # down
                dfs(r - 1, c, i + 1) or # up
                dfs(r, c + 1, i + 1) or # right
                dfs(r, c - 1, i + 1)    # left
            )

            path.remove((r, c)) # untrack

            return res

        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True
        return False