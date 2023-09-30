""" 70 ms (beats 93.39%), 34.2 MB (beats 72.33%) """

from functools import cache


@cache
def solve(s: str, t: str) -> int:
    n = len(s)
    m = len(t)

    if n < m:
        return 0
    elif n == m:
        return 1 if s == t else 0
    elif m == 0:
        return 1

    acc = solve(s[1:], t)

    if s[0] == t[0]:
        acc += solve(s[1:], t[1:])

    return acc


if __name__ == "__main__":

    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("rabbbit", "rabbit"), 3)
    test(("babgbag", "bag"), 5)
