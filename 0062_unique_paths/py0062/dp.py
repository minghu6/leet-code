""" O(mn), 46 ms (beats 44.10%), 16.4 MB (beats 48.70%) """

from functools import cache

@cache
def solve(m: int, n: int) -> int:
    if m == 1:
        return 1

    return sum([solve(m-1, i) for i in range(1, n+1)])




if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test((3, 7), 28)
    test((3, 2), 3)
