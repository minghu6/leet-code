""" 52 ms (beats 44.28%, ~100%), 21.06 MB (beats 31.05%) """

from enum import Enum, auto
from functools import cache
from typing import List

class Mode(Enum):
    Buy = auto(),
    Sell = auto()

def solve(prices: List[int]) -> int:
    n = len(prices)

    @cache
    def recur(mode: Mode, i: int) -> int:
        if i >= n:
            return 0

        if mode is Mode.Buy:
            cand1 = -prices[i] + recur(Mode.Sell, i+1)
            cand2 = recur(Mode.Buy, i+1)
        else:
            cand1 = prices[i] + recur(Mode.Buy, i+2)
            cand2 = recur(Mode.Sell, i+1)

        return max(cand1, cand2)

    return recur(Mode.Buy, 0)



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([1,2,3,0,2], 3)
    test([1], 0)
