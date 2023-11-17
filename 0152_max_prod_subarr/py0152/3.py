""" 80 ms (beats 54.67%, ~100%), 16.76 MB (~100%) """

from typing import List

def solve(nums: List[int]) -> int:
    prefix = postfix = 0
    ans = nums[0]

    for i in range(len(nums)):
        if prefix == 0:
            prefix = nums[i]
        else:
            prefix *= nums[i]

        if postfix == 0:
            postfix = nums[~i]
        else:
            postfix *= nums[~i]

        ans = max(ans, prefix, postfix)

    return ans
