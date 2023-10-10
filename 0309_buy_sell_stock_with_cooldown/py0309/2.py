""" 45 ms (beats 79.16%, ~100%), 16.56 MB (beats 87.33%. ~100%) """

from typing import List


def solve(prices: List[int]) -> int:
    n = len(prices)

    if n == 1:
        return 0

    prices.append(0)

    buy0 = -prices[0]
    buy1 = max(buy0, -prices[1])
    sell0 = 0

    for i in range(n-1):
        buy2 = max(buy1, sell0 - prices[i + 2])
        sell1 = max(sell0, buy0 + prices[i + 1])

        sell0 = sell1
        buy1, buy0 = buy2, buy1

    return sell0


if __name__ == "__main__":

    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([1,2,4], 3)
    test([1, 2, 3, 0, 2], 3)
    test([1], 0)
