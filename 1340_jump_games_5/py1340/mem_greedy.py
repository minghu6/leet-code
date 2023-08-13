""" O(n) 152ms (beats 98.41%), 19.52 mb beats 42.46%
The origin idea comes from @gd303 (improved a little by me)
"""

from typing import List, Iterator
from functools import cache


def solve(arr: List[int], d: int) -> int:
    n = len(arr)

    forward = [-1] * n
    backward = [-1] * n

    def build(range: Iterator[int], storage: List[int]):
        stack = []

        for i in range:
            while stack and arr[stack[-1]] < arr[i] and abs(stack[-1] - i) <= d:
                storage[stack.pop()] = i
            stack.append(i)

    build(range(n), forward)
    build(range(n-1, -1, -1), backward)

    @cache
    def backtrace(i: int) -> int:
        if i == -1:
            return 0

        return max(backtrace(forward[i]), backtrace(backward[i])) + 1

    return max(map(backtrace, range(n)))


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2), 4)
    test(([7, 6, 5, 4, 3, 2, 1], 1), 7)
    test(([3, 3, 3, 3, 3], 3), 1)
    test(([22, 29, 52, 97, 29, 75, 78, 2, 92, 70, 90,
         12, 43, 17, 97, 18, 58, 100, 41, 32], 17), 6)
