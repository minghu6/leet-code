""" 771 ms (beats 21.15%, ~100%), 19.41 MB (beats 85.77%, ~100%) """

from typing import List


def solve(matrix: List[List[str]]) -> int:
    n = len(matrix[0])
    h = [0] * n
    ans = 0

    for row in matrix:
        for i in range(n):
            if row[i] == '0':
                h[i] = 0
            else:
                h[i] += 1

        lw = [1] * n
        rw = [1] * n

        for i in range(n):
            if h[i]:
                j = i-1

                while j >= 0 and h[j] >= h[i]:
                    lw[i] += lw[j]
                    j -= lw[j]

        for i in range(n-1, -1, -1):
            if h[i]:
                j = i+1

                while j < n and h[j] >= h[i]:
                    rw[i] += rw[j]
                    j += rw[j]

        for i in range(n):
            if h[i]:
                ans = max(ans, min(h[i], (lw[i]+rw[i]-1)) ** 2)

    return ans


if __name__ == "__main__":

    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

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
