from typing import *
from bisect import insort
from sortedcontainers import SortedList


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        return solve(buildings)


def solve(buildings: List[List[int]]) -> List[List[int]]:
    x_data = [l for (l, _, _) in buildings]

    for (_, r, _) in buildings:
        insort(x_data, r)

    queue = SortedList([], key=lambda x: x[1])
    i = 0
    res = []
    n_buildings = len(buildings)

    for x in x_data:
        while i < n_buildings and buildings[i][0] == x:
            queue.add((buildings[i][1], buildings[i][2]))
            i += 1

        # pop outdated from priority queue

        while queue and queue[-1][0] <= x:
            queue.pop()

        if queue:
            h = queue[-1][1]
        else:
            h = 0

        if not res or res[-1][1] != h:
            res.append([x, h])

    return res


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
