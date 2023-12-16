""" 78 ms (beats 39.60%, ~100%), 20.21 MB (beats 5.06%) """

from functools import cache
from typing import List


def solve(dungeon: List[List[int]]) -> int:
    m = len(dungeon)
    n = len(dungeon[0])

    @cache
    def dfs(i, j):
        if i >= m or j >= n:
            return -float('inf')

        if i == m-1 and j == n-1:
            return dungeon[i][j]
        else:
            nx = max(dfs(i+1, j), dfs(i, j+1))

            if nx < 0:
                return dungeon[i][j] + nx
            else:
                return dungeon[i][j]

    return 1+max(-dfs(0, 0), 0)



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([[-2,-3,3],[-5,-10,1],[10,30,-5]], 7)
