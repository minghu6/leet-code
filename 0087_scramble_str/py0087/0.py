""" 58 ms (beats 78.15%, ~100%), 17.9 MB (beats 36.12%, ~100%) """

from functools import cache


@cache
def solve(s1: str, s2: str) -> bool:
    if sorted(s1) != sorted(s2):
        return False

    n = len(s1)

    if n == 1:
        return s1 == s2

    for i in range(1, n):
        if (
            solve(s1[:i], s2[n - i :])
            and solve(s1[i:], s2[: n - i])
            or solve(s1[:i], s2[:i])
            and solve(s1[i:], s2[i:])
        ):
            return True

    return False


if __name__ == "__main__":

    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("great", "rgeat"), True)
    test(("abcde", "caebd"), False)
    test(("a", "a"), True)
