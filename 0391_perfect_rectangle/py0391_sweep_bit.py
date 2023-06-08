from typing import *
from sortedcontainers import SortedList, SortedSet


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        return solve(rectangles)


def solve(rectangles: List[List[int]]) -> bool:
    area_sum = 0

    y_data = SortedSet()

    for _, y, _, b in rectangles:
        y_data.add(y)
        y_data.add(b)

    y_map = { y: i for i, y in enumerate(y_data)}

    ent = SortedList(key=lambda x: x[0])
    ex = SortedList(key=lambda x: x[0])

    for x, y, a, b in rectangles:
        area_sum += (a-x) * (b-y)

        y = y_map[y]
        b = y_map[b]

        ent.add((x, y, b))
        ex.add((a, y, b))

    del y_map

    min_x = ent[0][0]
    max_a = ex[-1][0]
    min_y = y_data[0]
    max_b = y_data[-1]

    cover_area = (max_a - min_x) * (max_b - min_y)

    if area_sum != cover_area:
        return False

    cobit = CoBIT(len(y_data))

    j = 0
    j_end = len(ex)

    for x, y, b in ent:
        while j < j_end and ex[j][0] <= x:
            cobit.update(ex[j][1], ex[j][2]-1, -1)
            j += 1

        if cobit.query(y, b-1) > 0:
            return False

        cobit.update(y, b-1, 1)

    return True


class CoBIT:
    """Range Update & Range Query"""

    def __init__(self, range_len: int) -> None:
        self.b1 = [0] * range_len
        self.b2 = [0] * range_len

    def update(self, l: int, r: int, x: int):
        """range add x for [l, r]"""

        CoBIT._add(self.b1, l, x)
        CoBIT._add(self.b1, r+1, -x)

        CoBIT._add(self.b2, l, (l-1) *x)
        CoBIT._add(self.b2, r+1, -r*x)

    def query(self, l: int, r: int) -> int:
        return self.prefix(r) - self.prefix(l-1)

    def prefix(self, i :int) -> int:
        return CoBIT._prefix(self.b1, i) * i - CoBIT._prefix(self.b2, i)

    @staticmethod
    def _add(bit: List[int], i: int, x: int):
        while i < len(bit):
            bit[i] += x
            i += (i+1) & -(i+1)

    @staticmethod
    def _prefix(bit: List[int], i: int) -> int:
        acc = 0

        while i >= 0:
            acc += bit[i]
            i -= (i+1) & -(i+1)

        return acc


if __name__ == '__main__':
    i = 0

    def test(input, expect):
        global i

        res = solve(input)
        assert res == expect
        print(f"pass{i}")
        i += 1

    test([[0,0,1,1],[0,1,3,2],[1,0,2,2]], False)

    test([[0,0,1,1],[0,0,1,1],[1,1,2,2],[1,1,2,2]], False)

    test([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]], False)

    test([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]], False)

    test([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]], True)
