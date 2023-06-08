from typing import *
from collections import Counter


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        return solve(rectangles)


def solve(rectangles: List[List[int]]) -> bool:
    vertexs = Counter()
    min_x = float("inf")
    min_y = float("inf")
    max_a = 0
    max_b = 0
    area_sum = 0

    for x, y, a, b in rectangles:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_a = max(max_a, a)
        max_b = max(max_b, b)

        vertexs[(x, y)] += 1
        vertexs[(a, y)] += 1
        vertexs[(x, b)] += 1
        vertexs[(a, b)] += 1

        area_sum += (a-x) * (b-y)

    cover_area = (max_a - min_x) * (max_b - min_y)

    if area_sum != cover_area:
        return False

    for (x0, y0), c in vertexs.items():
        if x0 in (min_x, max_a) and y0 in (min_y, max_b):
            if c != 1:
                return False
        elif x0 in (min_x, max_a) or y0 in (min_y, max_b):
            if c != 2:
                return False
        else:
            if c not in (2, 4):
                return False

    return True


if __name__ == '__main__':
    i = 0

    def test(input, expect):
        global i

        res = solve(input)
        assert res == expect
        print(f"pass{i}")
        i += 1

    test([[0,0,1,1],[0,0,1,1],[1,1,2,2],[1,1,2,2]], False)

    test([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]], False)

    test([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]], False)

    test([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]], True)
