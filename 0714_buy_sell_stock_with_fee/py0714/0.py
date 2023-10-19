""" 566 ms (beats 77%, ~100%), 23.7 MB (beats 67.29%, ~100%) """

from typing import List


def solve(prices: List[int], fee: int) -> int:
    n = len(prices)
    buy = -prices[0]
    sell = 0

    for price in prices[1:]:
        buy1 = max(buy, sell-price)
        sell1 = max(sell, buy+price-fee)

        buy = buy1
        sell = sell1

    return sell



if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([1,3,2,8,4,9], 2), 8)
    test(([1,3,7,5,10,3], 3), 6)
