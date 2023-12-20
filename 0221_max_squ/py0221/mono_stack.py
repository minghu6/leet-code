""" 596 ms (beats 67.28%, ~100$), 19.2 MB (beats 85.77%, ~100%) """

from typing import List


def solve(matrix: List[List[str]]) -> int:
    n = len(matrix[0])
    h = [0] * (n+1)
    ans = 0

    for row in matrix:
        for i in range(n):
            if row[i] == '0':
                h[i] = 0
            else:
                h[i] += 1

        pos = [-1]

        for i in range(n+1):
            while h[i] < h[pos[-1]]:
                top = pos.pop()

                while h[pos[-1]] == h[top]:
                    pos.pop()

                w = i-pos[-1]-1

                ans = max(ans, min(w, h[top]) ** 2)

            pos.append(i)

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
