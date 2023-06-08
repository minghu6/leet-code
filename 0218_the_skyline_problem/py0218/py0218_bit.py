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

    #bit = RevBIT(len(x_data))
    bit = FakeBIT(len(x_data))

    # Sweep Line

    res = []
    j = 0

    for i, x in enumerate(x_data):
        while j < len(buildings) and x == buildings[j][0]:
            r, h = buildings[j][1:3]

            bit.update(x_map[r]-1, h, until=i)

            j += 1

        h = bit.suffix(x_map[x])

        if not res or res[-1][1] != h:
            res.append([x, h])

    return res


class RevBIT():
    """Reversed Binary Indexed Tree"""

    def __init__(self, data_len: int):
        # base 0
        self.data = [0] * data_len

    def update(self, i: int, val: int, until: int) -> None:
        while i >= until:
            self.data[i] = max(self.data[i], val)

            i -= (len(self.data) - i - 1) & -(len(self.data) - i - 1)

    def suffix(self, i: int) -> int:
        """suffix"""
        acc = 0

        while True:
            acc = max(acc, self.data[i])

            l = (len(self.data) - i - 1) & -(len(self.data) - i - 1)
            if l == 0:
                break
            i += l


        return acc


class FakeBIT():
    """Fake Binary Indexed Tree whose prefix for update and suffix for query"""

    def __init__(self, data_len: int):
        # base 0
        self.data = [0] * data_len

    def update(self, i: int, val: int, until: int) -> None:
        while i >= until:
            self.data[i] = max(self.data[i], val)

            i -= (i + 1) & -(i + 1)

    def suffix(self, i: int) -> int:
        acc = 0

        while i < len(self.data):
            acc = max(acc, self.data[i])

            i += (i + 1) & -(i + 1)

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
