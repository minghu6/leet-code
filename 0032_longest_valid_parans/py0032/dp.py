from typing import List


def solve(s: str) -> int:
    if not s:
        return 0

    dp = [0] * len(s)

    for i in range(1, len(s)):
        if s[i] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
            dp[i] = 2 + dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else 0)

    return max(dp)


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test("(()(((()", 2)
    test("()(()", 2)
    test("(()", 2)
    test(")()())", 4)
    test("", 0)
