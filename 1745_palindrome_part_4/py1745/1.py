

from functools import cache


def solve(s: str) -> bool:
    n = len(s)

    @cache
    def p(i, j):
        if j-i == 0:
            return True
        elif j-i == 1:
            return s[i] == s[j]
        else:
            return s[i] == s[j] and p(i+1, j-1)

    for i in range(n-2):
        if p(0, i):
            for j in range(i+1, n-1):
                if p(i+1, j) and p(j+1, n-1):
                    return True

    return False


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test("abcbdd", True)
    test("bcbddxy", False)
