""" O(n^2) TLE! ms (beats %),  MB (beats %) """

from typing import List
from itertools import accumulate


def solve(nums: List[int]) -> int:
    max_v = max(nums)

    if max_v <= 0:
        return max_v

    nums = compress(nums)
    n = len(nums)

    pref_sum = list(accumulate(nums))
    ans = max(pref_sum)

    for i in range(1, n):
        if nums[i] < 0:
            continue
        for j in range(i, n):
            ans = max(ans, pref_sum[j]-pref_sum[i-1])

    return ans

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
