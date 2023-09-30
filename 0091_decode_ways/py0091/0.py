"""  ms (beats %),  MB (beats %) """

from functools import cache


def solve(s: str) -> int:
    n = len(s)

    @cache
    def recur(i: int) -> int:
        if i == n-1:
            if s[i] == '0':
                return 0
            else:
                return 1
        elif i == n:  # end
            return 1

        if s[i] == '0':
            return 0
        if s[i] == '1' or s[i] == '2' and '0' <= s[i+1] <= '6':
            return recur(i+2) + recur(i+1)
        else:
            return recur(i+1)

    return recur(0)



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test("12", 2)
    test("226", 3)
    test("06", 0)
    test("0", 0)
