# blueprint
# def solve(s: str, p: str) -> bool:
#     # Traping: [[False] * (len(p)+1)] * (len(s)+1)
#     dp = [ [False] * (len(p)+1) for i in range(len(s)+1) ]

#     dp[0][0] = True
#     for j in range(1, len(p)+1):
#         if p[j-1] == '*':
#             dp[0][j] = dp[0][j-1]

#     for i in range(1, len(s)+1):
#         for j in range(1, len(p)+1):
#             if p[j-1] == '*':
#                 dp[i][j] = dp[i-1][j] or dp[i][j-1]
#             else:
#                 dp[i][j] = dp[i-1][j-1] and (p[j-1] == '?' or p[j-1] == s[i-1])

#     return dp[-1][-1]

# Improved
# def solve(s: str, p: str) -> bool:
#     dp = [False] * (len(p)+1)

#     # i = 0
#     dp[0] = True

#     for j in range(1, len(p)+1):
#         if p[j-1] == '*':
#             dp[j] = dp[j-1]

#     for i in range(1, len(s)+1):
#         prev1 = dp[0]
#         dp[0] = False

#         for j in range(1, len(p)+1):
#             prev0 = dp[j]

#             if p[j-1] == '*':
#                 dp[j] = prev0 or dp[j-1]
#             else:
#                 dp[j] = prev1 and (p[j-1] == '?' or p[j-1] == s[i-1])

#             prev1 = prev0

#     return dp[-1]


def solve(s: str, p: str) -> bool:
    """ same with module fnmatch """
    dp = [False] * (len(s)+1)

    # j = 0
    dp[0] = True

    for j in range(1, len(p)+1):
        if p[j-1] == '*':
            for i in range(1, len(s)+1):
                dp[i] = dp[i-1] or dp[i]
        elif p[j-1] == '?':
            prev1 = dp[0]
            dp[0] = False

            for i in range(1, len(s)+1):
                dp[i], prev1 = prev1, dp[i]
        else:
            prev1 = dp[0]
            dp[0] = False

            for i in range(1, len(s)+1):
                if s[i-1] == p[j-1]:
                    dp[i], prev1 = prev1, dp[i]
                else:
                    prev1 = dp[i]
                    dp[i] = False

    return dp[-1]


if __name__ == '__main__':
    def test(s, p, expect):
        found = solve(s, p)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test('aa', 'a', False)
    test('aa', '*', True)
    test('cb', '?a', False)

