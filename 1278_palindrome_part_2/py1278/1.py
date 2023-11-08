""" 71 ms (beats 94.85%, ~100%), 17.26 MB (beats 51.03%) """

from functools import cache


def solve(s: str, k: int) -> int:
    n = len(s)

    @cache
    def recur(i, j) -> int:
        if j == 1:
            return p(i, n-1)
        elif j == n-i:
            return 0
        else:
            return min(p(i, c) + recur(c+1, j-1) for c in range(i, n-(j-1)))

    @cache
    def p(i, j) -> int:
        if j-i == 0:
            return 0
        elif j-i == 1:
            return (0 if s[i] == s[j] else 1)
        else:
            return (0 if s[i] == s[j] else 1) + p(i+1, j-1)

    return recur(0, k)


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("ssxufzteudvxliwwwkda", 5), 6)
    test(("aabbc", 3), 0)
    test(("tcymekt", 4), 2)
    test(("abc", 2), 1)
    test(("leetcode", 8), 0)
