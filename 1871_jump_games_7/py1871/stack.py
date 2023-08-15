""" O(n) 201 ms (beats 96.49%), 20.50 MB (beats 48.76%) """

from collections import deque
from itertools import islice


def solve(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    stack = deque([0])

    for i, v in islice(enumerate(s), 1, None):
        if v == '0':
            while stack and stack[0] < i-maxJump:
                stack.popleft()

            if not stack:
                return False

            if stack[0] <= i-minJump:
                stack.append(i)

    return bool(stack) and stack[-1] == n-1


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("011010", 2, 3), True)
    test(("01101110", 2, 3), False)
