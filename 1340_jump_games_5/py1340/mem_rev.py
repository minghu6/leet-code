""" better O(dn), 199 ms (beats 88.3%), 16.9 MB (beats 73.24%)
It's an improved memorization's algorithm implementaion.
"""

from typing import List
from itertools import chain


def solve(arr: List[int], d: int) -> int:
    n = len(arr)

    ans_cache = [1] * n
    forward_cache = [0] * n
    backward_cache = [0] * n

    data = sorted(enumerate(arr), key=lambda x: x[1])

    for i, v in data:
        # d >= 1

        r = 0

        while i+r+1 < n and r < d and arr[i+r+1] < v:
            r += forward_cache[i+r+1] + 1

        forward_cache[i] = min(r, d)

        l = 0

        while i-l > 0 and l < d and arr[i-l-1] < v:
            l += backward_cache[i-l-1] + 1

        backward_cache[i] = min(l, d)

        ans_cache[i] += max(chain(ans_cache[i-l:i], ans_cache[i+1:i+r+1]), default=0)

    return max(ans_cache)


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2), 4)
    test(([7, 6, 5, 4, 3, 2, 1], 1), 7)
    test(([3, 3, 3, 3, 3], 3), 1)
    test(([22, 29, 52, 97, 29, 75, 78, 2, 92, 70, 90,
         12, 43, 17, 97, 18, 58, 100, 41, 32], 17), 6)

