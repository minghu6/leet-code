""" 56 ms (beats 23.68%), 16.8 MB (beats 7.1%, ~100%) """

from typing import List
from functools import cache


def solve(obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    @cache
    def dp(i: int, j: int) -> int:
        if obstacleGrid[i-1][j-1]:
            return 0

        if i == 1 and j == 1:
            return 1

        if i == 1:
            return dp(i, j-1)
        elif j == 1:
            return dp(i-1, j)
        else:
            return dp(i, j-1) + dp(i-1, j)

    return dp(m, n)


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([[0,0,0],[0,1,0],[0,0,0]], 2)
    test([[1,0]], 0)
    test([[0,1],[0,0]], 1)
