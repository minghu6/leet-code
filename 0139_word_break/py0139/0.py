""" 42 ms (beats 71.9%), 16.8 MB (beats 8.41%, ~100%) """

from typing import List


def solve(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    w_set = set()
    w_len_set = set()

    for w in wordDict:
        if len(w) < n:
            w_len_set.add(len(w))
            w_set.add(w)

    def dfs(i: int) -> bool:
        if i == n:
            return True

        return any(s[i:i+l] in w_set and dfs(i+l) for l in w_len_set)

    return dfs(0)



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(())
