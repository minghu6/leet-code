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

    segtree = SegmentTree(len(y_data))

    j = 0
    j_end = len(ex)

    for x, y, b in ent:
        while j < j_end and ex[j][0] <= x:
            segtree.update(ex[j][1], ex[j][2]-1, False)
            j += 1

        try:
            segtree.update(y, b-1, True)
        except:
            return False

    return True


class SegmentTree:
    """DFS型"""

    def __init__(self, range_len: int):
        self.marked = [0] * range_len * 2
        self.root = (0, range_len - 1, 0)

    def update(self, l: int, r: int, val: bool):
        """It would raise when try to mark an occupied position"""
        self._update(l, r, val, *self.root)

    def _update(self, l: int, r: int, val: bool, tl: int, tr: int, i: int):
        if l > r:
            return

        range_len = tr - tl + 1

        if l == tl and r == tr:
            if val and self.marked[i] > 0:
                # can't catch class don't inherrit from BaseException
                # however so what we could use except to catch
                raise "Occupied"

            if val:
                self.marked[i] = range_len
            else:
                self.marked[i] = 0
        else:
            mid = (tl + tr) // 2
            sub_l = (mid - tl + 1)

            if val and self.marked[i] == range_len:
                raise "Occupied"

            self._update(l, min(r, mid), val, tl, mid, i+1)
            self._update(max(mid+1, l), r, val, mid+1, tr, i+2*sub_l)

            self.marked[i] = self.marked[i+1] + self.marked[i+2*sub_l]


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
