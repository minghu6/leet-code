""" O(n), 773 ms (Beats 97.14%), 30.53 MB (Beats 52.38%) """

from typing import List
from collections import deque

def solve(nums: List[int], k: int) -> int:
    n = len(nums)

    q = deque([0])
    dp = [0] * n

    dp[0] = nums[0]

    for i in range(1, n):
        if i-q[0] > k:
            q.popleft()

        dp[i] = nums[i] + dp[q[0]]

        while q and dp[q[-1]] <= dp[i]:
            q.pop()

        q.append(i)

    return dp[-1]




if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([100,-1,-100,-1,100], 2), 198)
    test(([1,-1,-2,4,-7,3], 2), 7)
    test(([10,-5,-2,4,0,3], 3), 17)
    test(([1,-5,-20,4,-1,3,-6,-3], 2), 0)
