""" O(n) 120ms (beats 100%), 16.6mb (beats 96.6%) """

from typing import List


max_int = 100_000 + 1

def solve(arr: List[int], d: int) -> int:
    arr.append(max_int)

    n = len(arr)

    stack = []
    dp = [1] * n

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            isoheight = [stack.pop()]

            while stack and arr[stack[-1]] == arr[isoheight[0]]:
                isoheight.append(stack.pop())

            for j in isoheight:
                if i-j <= d:
                    dp[i] = max(dp[i], dp[j]+1)

                if stack and j-stack[-1] <= d:
                    dp[stack[-1]] = max(dp[stack[-1]], dp[j]+1)

        stack.append(i)

    return max(dp[:-1])


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2), 4)
    test(([7, 6, 5, 4, 3, 2, 1], 1), 7)
    test(([3, 3, 3, 3, 3], 3), 1)
    test(([22, 29, 52, 97, 29, 75, 78, 2, 92, 70, 90,
         12, 43, 17, 97, 18, 58, 100, 41, 32], 17), 6)
