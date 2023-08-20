""" O(n) 622 ms (beats 74.97%), 30.42 MB (beats 83.1%) """

from typing import List


def solve(nums: List[int]) -> int:
    max_v = max(nums)

    if max_v <= 0:
        return max_v

    nums = compress(nums)
    max_unit = max(nums)  # get max positive unit

    # Onion Transform

    max_seq = 0

    while len(nums) >= 3:
        if nums[-1] <= 0:
            nums.pop()
        else:
            layer = nums.pop() + nums.pop()

            if layer > 0:
                nums[-1] += layer

            max_seq = max(max_seq, nums[-1])

    max_seq = max(max_seq, sum(nums))

    return max(max_unit, max_seq)


def compress(nums: List[int]) -> List[int]:
    n = len(nums)

    nums2 = []
    i = 0

    while i < n:
        acc = 0

        if nums[i] >= 0:
            while i < n and nums[i] >= 0:
                acc += nums[i]
                i += 1
        else:
            while i < n and nums[i] < 0:
                acc += nums[i]
                i += 1

        nums2.append(acc)

    return nums2


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([-2,1,-3,4,-1,2,1,-5,4], 6)
    test([1], 1)
    test([5,4,-1,7,8], 23)
