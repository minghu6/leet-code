

from typing import List


def solve(nums: List[int]) -> int:
    acc_max = acc_min = 1
    ans = nums[0]

    for v in nums:
        cmp = [acc_min*v, acc_max*v, v]
        cmp.sort()

        acc_min = cmp[0]
        acc_max = cmp[2]

        if acc_max > ans:
            ans = acc_max

    return ans
