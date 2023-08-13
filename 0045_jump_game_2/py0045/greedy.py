""" O(n) 120ms (beats 96.35%) """

from typing import List


def solve(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0

    i0 = 0  # prev i
    i = nums[i0]
    step = 1

    while i < len(nums) - 1:
        i0, i = max(
            [(j, j+nums[j]) for j in range(i0+1, i0+1+nums[i0])],
            key=lambda x: x[1]
        )

        step += 1

    return step



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([2,3,1,1,4], 2)
    test([2,3,0,1,4], 2)

