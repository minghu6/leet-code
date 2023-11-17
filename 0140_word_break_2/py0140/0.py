"""  ms (beats %),  MB (beats %) """

from typing import List


def solve(s: str, wordDict: List[str]) -> List[str]:
    n = len(s)

    dp = [[] for i in range(n+1)]
    dp[0].append([])

    for i in range(n):
        for w in wordDict:
            l = len(w)

            if i+1-l >= 0 and s[i+1-l:i+1] == w:
                for case in dp[i+1-l]:
                    dp[i+1].append(case + [w])

    return [' '.join(case) for case in dp[n]]



if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("catsanddog", ["cat","cats","and","sand","dog"]), ["cats and dog","cat sand dog"])
