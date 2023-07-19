from typing import List
from collections import defaultdict


def solve(arr: List[int], difference: int) -> int:
    k = difference
    dp = defaultdict(lambda: 0)

    for v in arr:
        dp[v] = dp[v-k] + 1

    return max(dp.values())



if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([1, 2, 3, 4], 1), 4)
    test(([1, 3, 5, 7], 1), 1)
    test(([1,5,7,8,5,3,4,2,1], -2), 4)
