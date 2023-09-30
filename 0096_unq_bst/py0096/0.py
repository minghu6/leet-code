"""  ms (beats %),  MB (beats %) """

from functools import cache

# max_n = 19

@cache
def solve(n: int) -> int:
    match n:
        case 0 | 1:
            return 1
        case _:
            acc = 0

            for i in range(0, (n-1+1)//2):
                acc += solve(i) * solve(n-1-i)

            ans = acc * 2

            if (n-1)%2 == 0:
                ans += solve((n-1)//2) ** 2

            return ans


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(3, 5)
    test(1, 1)
