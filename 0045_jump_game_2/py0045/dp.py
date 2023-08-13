""" O(n^2) 3862ms (beats 25.91%) """

from typing import List


def solve(nums: List[int]) -> int:
    dp = [len(nums)] * len(nums)

    dp[0] = 0

    for i in range(0, len(nums)-1):
        for j in range(i+1, min(i+nums[i]+1, len(nums))):
            dp[j] = min(dp[j], dp[i]+1)

    return dp[-1]



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([2,3,1,1,4], 2)
    test([2,3,0,1,4], 2)
