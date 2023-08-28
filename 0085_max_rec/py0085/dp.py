""" 282 ms (beats 55.4%, ~100%),  17.56 MB (beats 92.49%) """

from typing import List


def solve(matrix: List[List[str]]) -> int:
    n = len(matrix[0])

    h = [0] * n
    ans = 0

    for row in matrix:
        for i in range(n):
            if row[i] == "1":
                h[i] += 1
            else:
                h[i] = 0

        pref = [1] * n
        suff = [1] * n

        for i in range(n):
            if h[i]:
                while i-pref[i] >= 0 and h[i-pref[i]] >= h[i]:
                    pref[i] += pref[i-pref[i]]

            i2 = n-1-i

            if h[i2]:
                while i2+suff[i2] < n and h[i2+suff[i2]] >= h[i2]:
                    suff[i2] += suff[i2+suff[i2]]


        ln_ans = max([(pref[i] + suff[i] - 1) * h[i] for i in range(n)])

        if ln_ans > ans:
            ans = ln_ans

    return ans


if __name__ == "__main__":

    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(
        [
            ["0", "0", "0", "0", "0", "0", "1"],
            ["0", "0", "0", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1"],
            ["0", "0", "0", "1", "1", "1", "1"],
        ],
        9,
    )
    test(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ],
        6,
    )
    test([["0"]], 0)
    test([["1"]], 1)
