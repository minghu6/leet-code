""" 551 ms (beats 98.7%), 19.25 MB (beats 62.82%) """


from typing import List


def solve(matrix: List[List[str]]) -> int:
    n = len(matrix[0])
    w = 0

    # right-down corner

    dp0 = [0] * (n+1)
    dp1 = [0] * (n+1)

    for row in matrix:
        for i in range(1, n+1):
            if row[i-1] == '1':
                dp1[i] = min(dp1[i-1], dp0[i], dp0[i-1]) + 1
            else:
                dp1[i] = 0

        w = max(w, max(dp1))
        dp1, dp0 = dp0, dp1

    return w * w


if __name__ == "__main__":

    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([["1"]], 1)

    test(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ],
        4,
    )

    test([["0","1"],["1","0"]], 1)

    test([["0"]], 0)
