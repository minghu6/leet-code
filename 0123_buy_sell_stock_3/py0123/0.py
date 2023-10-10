""" 760 ms (beats 98.06%),  30.5 MB (beats 72.56%, ~100%) """

from typing import List


def solve(prices: List[int]) -> int:
    n = len(prices)

    dp = [0] * (n + 1)
    hi = prices[-1]

    for i in range(n - 2, -1, -1):
        if prices[i + 1] > hi:
            hi = prices[i + 1]

        if hi - prices[i] > dp[i + 1]:
            dp[i] = hi - prices[i]
        else:
            dp[i] = dp[i + 1]

    ans = dp[0]
    lo = prices[0]

    for i in range(1, n):
        if prices[i - 1] < lo:
            lo = prices[i - 1]

        if prices[i] - lo + dp[i + 1] > ans:
            ans = prices[i] - lo + dp[i + 1]

    return ans


if __name__ == "__main__":

    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 13)
