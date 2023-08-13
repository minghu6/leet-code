""" O(n) 549 ms (beats 98.59%), 29.6 MB beats 94.3% """

from typing import List
from collections import defaultdict

def solve(arr: List[int]) -> int:
    n = len(arr)
    val = defaultdict(list)

    for i, v in enumerate(arr):
        val[v].append(i)

    step = 0
    queue = [0] if arr[1:] else []
    visited = [False] * n

    while queue:
        nxt_queue = []
        step += 1

        for i in queue:
            if i+1 < n and not visited[i+1]:
                visited[i+1] = True
                nxt_queue.append(i+1)

                if i+1 == n-1:
                    return step

            if i-1 >= 0 and not visited[i-1]:
                visited[i-1] = True
                nxt_queue.append(i-1)

            while val[arr[i]]:
                j = val[arr[i]].pop()

                if not visited[j]:
                    visited[j] = True
                    nxt_queue.append(j)

                    if j == n-1:
                        return step

        queue = nxt_queue

    return step


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([100,-23,-23,404,100,23,23,23,3,404], 3)
    test([7], 0)
    test([7,6,9,6,9,6,9,7], 1)
