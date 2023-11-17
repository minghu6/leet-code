

from typing import List


def solve(s: str, wordDict: List[str]) -> bool:
    n = len(s)

    dp = [False] * (n+1)
    dp[0] = True

    for i in range(n):
        for w in wordDict:
            l = len(w)

            if i+1-l >= 0 and not dp[i+1]:
                dp[i+1] = dp[i+1-l] and s[i+1-l:i+1] == w

    return dp[n]


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("leetcode", ["leet","code"]), True)
