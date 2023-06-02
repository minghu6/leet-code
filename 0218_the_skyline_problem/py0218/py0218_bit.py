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

    # Build BIT by Batch Update

    bit = RevBIT(len(x_data))

    # Sweep Line

    res = []
    j = 0

    for i, x in enumerate(x_data):
        while j < len(buildings) and x == buildings[j][0]:
            bit.update(x_map[buildings[j][1]] - 1, buildings[j][2])
            j += 1

        h = bit.suffix(x_map[x])

        # print(h)

        if not res or res[-1][1] != h:
            res.append([x, h])

    return res


class RevBIT():
    """Binary Indexed Tree"""

    def __init__(self, data_len: int):
        # base 0
        self.data = [0] * data_len

    def update(self, i: int, val: int) -> None:
        while i >= 0:
            self.data[i] = max(self.data[i], val)

            i -= (i+1) & -(i+1)

    def suffix(self, i: int) -> int:
        acc = 0

        while i < len(self.data):
            acc = max(acc, self.data[i])

            i += (i+1) & -(i+1)

        return acc


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
