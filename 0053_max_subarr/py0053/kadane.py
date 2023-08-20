""" O(n) 592 ms (beats 87.39%), 30.56 MB (beats 51.70%) """

from typing import List
from itertools import accumulate


def solve(nums: List[int]) -> int:
    return max(accumulate(nums, lambda x, y: max(y, x+y)))


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([-2,1,-3,4,-1,2,1,-5,4], 6)
    test([1], 1)
    test([5,4,-1,7,8], 23)
