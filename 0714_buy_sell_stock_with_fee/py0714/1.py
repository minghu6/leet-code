""" 495 ms (beats 99.50%, ~100%), 23.7 MB (beats 67.29%, ~100%) """

from typing import List


def solve(prices: List[int], fee: int) -> int:
    buy = prices[0]+fee
    ans = 0

    for price in prices[1:]:
        if price + fee < buy:
            buy = price + fee
        elif price > buy:
            ans += price-buy
            buy = price

    return ans
