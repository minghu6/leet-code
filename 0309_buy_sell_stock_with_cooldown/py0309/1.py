""" 36 ms (beats 98.07%, ~100%), 16.39 MB (beats 99.34%) """

from typing import List


def solve(prices: List[int]) -> int:
    n = len(prices)

    if n == 1:
        return 0

    prices.append(0)
    buy = [0] * (n+1)
    buy[0] = -prices[0]
    buy[1] = max(buy[0], -prices[1])

    sell = [0] * n

    for i in range(n-1):
        buy[i + 2] = max(buy[i+1], sell[i] - prices[i + 2])
        sell[i + 1] = max(sell[i], buy[i] + prices[i + 1])

    return sell[n - 1]


if __name__ == "__main__":

    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([1,2,4], 3)
    test([1, 2, 3, 0, 2], 3)
    test([1], 0)
