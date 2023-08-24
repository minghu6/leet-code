""" 39 ms (beats 77.42%), 16.1 MB (beats 99.75%) """

from math import comb

def solve(m: int, n: int) -> int:
    return comb(m+n-2, m-1)




if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test((3, 7), 28)
    test((3, 2), 3)
