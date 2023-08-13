""" O(n*d), 421ms (beats 80.95%), 19.17mb (beats 54.37%)
It's an original memorization algorithm implementation.
"""

from typing import List
from itertools import chain, takewhile


def solve(arr: List[int], d: int) -> int:
    n = len(arr)
    cache = [0] * n

    def dfs(i: int) -> int:
        if cache[i]:
            return cache[i]

        subs = chain(
            takewhile(lambda j: arr[j] < arr[i], range(i-1, max(0, i-d)-1, -1)),
            takewhile(lambda j: arr[j] < arr[i], range(i+1, min(n-1, i+d)+1, 1)),
        )

        cache[i] = max(map(dfs, subs), default=0) + 1

        return cache[i]

    return max(map(dfs, range(n)))  # n >= 1






if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2), 4)
    test(([7, 6, 5, 4, 3, 2, 1], 1), 7)
    test(([3, 3, 3, 3, 3], 3), 1)
    test(([22, 29, 52, 97, 29, 75, 78, 2, 92, 70, 90,
         12, 43, 17, 97, 18, 58, 100, 41, 32], 17), 6)
