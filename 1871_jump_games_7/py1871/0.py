""" O(nlogn) 439 ms (beats 36.99%), 21.1 MB (beats 25.62%) """

from bisect import bisect_left


def solve(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    stack = [0]

    for i in range(1, n):
        if s[i] == '0':
            if i-maxJump <= stack[-1] and i-minJump >= 0:
                l = bisect_left(stack, i-maxJump)

                if stack[l] == i-maxJump:
                    stack.append(i)
                    continue

                r = bisect_left(stack, i-minJump)

                if l < r or stack[r] == i-minJump:
                    stack.append(i)
                    continue

    return stack[-1] == n-1


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("011010", 2, 3), True)
    test(("01101110", 2, 3), False)
