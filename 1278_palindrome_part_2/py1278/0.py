""" 120 ms (beats 73.20%), 16.34 MB (beats 94.33%, ~100%) """

from math import inf


def solve(s: str, k: int) -> int:
    n = len(s)

    p = [[0] * (n-i+1) for i in range(n)]

    # for i in range(n-1):
    #     p[i][1] = 0 if s[i] == s[i+1] else 1

    #     # even
    #     for r in range(1, min(i-1+1, n-1-(i+2)+1)+1):
    #         p[i-r][2*r+1] = p[i-r+1][2*r+1-2] + (0 if s[i-r] == s[i+1+r] else 1)

    #     # odd
    #     for r in range(1, min(i-1+1, n-1-(i+1)+1)+1):
    #         p[i-r][2*r] = p[i-r+1][2*r-2] + (0 if s[i-r] == s[i+r] else 1)

    for span in range(2, n+1):
        for i in range(n-span+1):
            p[i][span] = p[i+1][span-2] + (0 if s[i] == s[i+span-1] else 1)

    dp = [[0] * k for _ in range(n)]

    for i in range(1, n):
        dp[i][0] = p[0][i+1]

        for j in range(1, min(i+1, k)):
            dp[i][j] = inf

            for c in range(j, i+1):
                if dp[i][j] > dp[c-1][j-1] + p[c][i-c+1]:
                    dp[i][j] = dp[c-1][j-1] + p[c][i-c+1]

    return dp[n-1][k-1]



if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("ssxufzteudvxliwwwkda", 5), 6)
    test(("aabbc", 3), 0)
    test(("tcymekt", 4), 2)
    test(("abc", 2), 1)
    test(("leetcode", 8), 0)
