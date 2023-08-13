""" 6041ms (beats 8.5%) """

from typing import List


def solve(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True

    i0 = 0
    i = nums[i0]

    while i < len(nums) - 1:
        if i0 == i:
            return False

        if i0+nums[i0] >= len(nums) - 1:
            return True

        i0, i = max(
            map(lambda j: (j, j+nums[j]), range(i0+1, i0+1+nums[i0])),
            key=lambda x: x[1]
        )

    return True



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"


    test([2,3,1,1,4], True)
    test([3,2,1,0,4], False)
