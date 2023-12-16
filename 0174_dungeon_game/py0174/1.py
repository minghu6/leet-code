""" 69 ms (beats 81.50%, ~100%, 55ms), 17.5 MB (beats 63.73%, ~100%) """

from typing import List


def solve(dungeon: List[List[int]]) -> int:
    m = len(dungeon)
    n = len(dungeon[0])
    tot = m+n-1

    low0 = [dungeon[-1][-1]] * min(m, n)
    low1 = [0] * min(m, n)

    for l in range(2, tot+1):
        h = min(m, l)
        w = min(n, l)

        x0, y0 = l-w+1, w
        x1, y1 = h, l-h+1

        d_max = x1-x0

        if x0 == 1 and y1 == 1:  # 矩形前半场
            low1[0] = min(
                dungeon[m-x0][n-y0] + low0[0],
                dungeon[m-x0][n-y0]
            )
            low1[d_max] = min(
                dungeon[m-x1][n-y1] + low0[l-2],
                dungeon[m-x1][n-y1]
            )

            for d in range(1, d_max):
                x, y = x0+d, y0-d

                nx = max(low0[d-1], low0[d])

                if nx < 0:
                    low1[d] = dungeon[m-x][n-y] + nx
                else:
                    low1[d] = dungeon[m-x][n-y]

        elif x0 == 1:  # 宽矩形中间场
            low1[0] = min(
                dungeon[m-x0][n-y0] + low0[0],
                dungeon[m-x0][n-y0]
            )

            for d in range(1, d_max+1):
                x, y = x0+d, y0-d
                nx = max(low0[d-1], low0[d])

                if nx < 0:
                    low1[d] = dungeon[m-x][n-y] + nx
                else:
                    low1[d] = dungeon[m-x][n-y]

        elif y1 == 1:  # 高矩形中间场 (x0 != 1)
            low1[d_max] = min(
                dungeon[m-x1][n-y1] + low0[min(m, n)-1],
                dungeon[m-x1][n-y1]
            )

            for d in range(d_max):
                x, y = x0+d, y0-d

                nx = max(low0[d], low0[d+1])

                if nx < 0:
                    low1[d] = dungeon[m-x][n-y] + nx
                else:
                    low1[d] = dungeon[m-x][n-y]

        else:  # 矩形后半场
            for d in range(d_max+1):
                x, y = x0+d, y0-d

                nx = max(low0[d], low0[d+1])

                if nx < 0:
                    low1[d] = dungeon[m-x][n-y] + nx
                else:
                    low1[d] = dungeon[m-x][n-y]

        low0, low1 = low1, low0

    return 1+max(-low0[0], 0)


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([[-2,-3,3],[-5,-10,1],[10,30,-5]], 7)
