""" 428ms (beats 96.53%)  """

from typing import List


def solve(nums: List[int]) -> bool:
    to = 0

    for i in range(0, len(nums)-1):
        if i > to:
            return False

        if i+nums[i] >= len(nums)-1:
            return True

        to = max(to, i+nums[i])

    return to >= len(nums) - 1



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"


    test([2,3,1,1,4], True)
    test([3,2,1,0,4], False)
