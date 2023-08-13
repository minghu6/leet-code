""" 394ms (beats 98.95%)  """

from typing import List


def solve(nums: List[int]) -> bool:
    lf = len(nums) - 1

    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] >= lf:
            lf = i

    return lf == 0


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"


    test([2,3,1,1,4], True)
    test([3,2,1,0,4], False)
