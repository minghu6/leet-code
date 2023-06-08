from typing import *
from bisect import bisect_right


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        return solve(buildings)


def solve(buildings: List[List[int]]) -> List[List[int]]:
    # 数据离散化 (Discretization)

    x_data = [buildings[0][0]]

    for (l, _, _) in buildings[1:]:
        if x_data[-1] != l:
            x_data.append(l)

    for (_, r, _) in buildings:
        i = bisect_right(x_data, r)
        # i != 0 for right x-axis
        if x_data[i-1] != r:
            x_data.insert(i, r)

    x_map = {x: i for i, x in enumerate(x_data)}

    # Build Segment Tree by Batch Update

    segtree = SegmentTree(len(x_data))

    for (l, r, h) in buildings:
        l = x_map[l]
        r = x_map[r]

        segtree.assign(h, l, r-1)

    # Sweep Line

    res = []

    for i, x in enumerate(x_data):
        h = segtree.query(i, i)

        if not res or res[-1][1] != h:
            res.append([x, h])

    return res



class SegmentTree():
    """DFS Layout,
    left: i+1,
    right: 2+2l
    """

    def __init__(self, data_len: int):
        # Just ignore self.tree
        self.assigned = [0] * 2 * data_len
        self.root = [0, data_len - 1, 0]

    def assign(self, val: int, l: int, r: int) -> None:
        """Override the smaller value"""
        self._assign(val, l, r, *self.root)

    def _assign(self, val: int, l: int, r: int, tl: int, tr: int, i: int) -> None:
        if l > r:
            return

        if l == tl and r == tr:
            self.assigned[i] = max(self.assigned[i], val)
        else:
            mid = (tl + tr) // 2
            subl = mid - tl + 1

            self._assign(val, l, min(mid, r), tl, mid, i + 1)
            self._assign(val, max(mid + 1, l), r, mid + 1, tr, i + 2 * subl)

    def query(self, l: int, r: int) -> int:
        """query [l, r] -> (x, h)"""
        return self._query(l, r, *self.root)

    def _query(self, l: int, r: int, tl: int, tr: int, i: int) -> int:
        if l > r:
            return 0

        if l == tl and r == tr:
            return self.assigned[i]
        else:
            mid = (tl + tr) // 2
            subl = mid - tl + 1

            if self.assigned[i]:
                self.assigned[i + 1] = max(
                    self.assigned[i + 1],
                    self.assigned[i],
                )

                self.assigned[i + 2 * subl] = max(
                    self.assigned[i + 2 * subl],
                    self.assigned[i],
                )

                self.assigned[i] = 0

            lv = self._query(l, min(mid, r), tl, mid, i + 1)
            rv = self._query(max(mid + 1, l), r, mid + 1, tr, i + 2 * subl)

            return max(lv, rv)



if __name__ == '__main__':

    def test(buildings, expect):
        res = solve(buildings)
        assert res == expect, f"{res}"

    test([
        [2, 9, 10],
        [3, 7, 15],
        [5, 12, 12],
        [15, 20, 10],
        [19, 24, 8]
    ], [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])

    test([[0, 2, 3], [2, 5, 3]], [[0, 3], [5, 0]])

    test([[1, 2, 1], [1, 2, 2], [1, 2, 3]], [[1, 3], [2, 0]])
