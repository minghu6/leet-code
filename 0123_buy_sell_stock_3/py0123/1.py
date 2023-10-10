""" 670 ms (beats 99.76%), 30.5 MB (beats 88.72%, ~100%) """


from typing import List


def solve(prices: List[int]) -> int:
    buy1 = -prices[0]
    sell1 = 0  # prices[0]+buy1
    buy2 = -prices[0]
    sell2 = 0  # prices[0]+buy2

    for price in prices[1:]:
        if buy1 < -price:
            buy1 = -price
        if sell1 < buy1+price:
            sell1 = buy1+price
        if buy2 < sell1-price:
            buy2 = sell1-price
        if sell2 < buy2+price:
            sell2 = buy2+price

    return sell2


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([1,2,4,2,5,7,2,4,9,0], 13)
