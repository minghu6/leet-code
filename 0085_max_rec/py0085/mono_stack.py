""" 234 ms (beats 97.39%, ~100%), 17.65 MB (beats 70.19%) """

from typing import List


def solve(matrix: List[List[str]]) -> int:
    n = len(matrix[0])

    h = [0] * (n+1)  # sentinel: h[n] = 0
    ans = 0

    for row in matrix:
        for i in range(n):
            if row[i] == "1":
                h[i] += 1
            else:
                h[i] = 0

        stack = [-1]  # sentinel: stack[0] = -1

        for i in range(n+1):
            while h[stack[-1]] > h[i]:
                top = stack.pop()

                while h[stack[-1]] == h[top]:
                    stack.pop()

                cand = h[top] * (i-stack[-1]-1)

                if ans < cand:
                    ans = cand

            stack.append(i)

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
