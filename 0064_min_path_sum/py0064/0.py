"""  ms (beats %),  MB (beats %) """

from typing import List
from functools import cache


def solve(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    @cache
    def dp(i: int, j: int) -> int:
        if i == 1 and j == 1:
            return grid[0][0]
        elif i == 1:
            return dp(i, j-1) + grid[i-1][j-1]
        elif j == 1:
            return dp(i-1, j) + grid[i-1][j-1]
        else:
            return min(dp(i, j-1), dp(i-1, j)) + grid[i-1][j-1]

    return dp(m, n)


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7)
    test([[1, 2, 3], [4, 5, 6]], 12)
