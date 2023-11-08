""" 507 ms (beats 99.22%, ~100%), 36.4 MB (beats 7.38%) """

from typing import List

def solve(s: str) -> List[List[str]]:
    n = len(s)

    cache = [[[]]]
    # p = [True] * n

    for i in range(1, n+1):
        ans = []

        for j in range(i):
            # if s[i-1] == s[j] and (i-1-j < 2 or p[j+1]):
            if s[i:j] == s[i:j][::-1]:
                # p[j] = True
                for case in cache[j]:
                    l = case.copy()
                    l.append(s[j:i])
                    ans.append(l)
            # else:
            #     p[j] = False

        cache.append(ans)

    return cache[n]



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert sorted(found) == sorted(expect), f"expect: {expect}, however found: {found}"

    test("aab", [["a","a","b"],["aa","b"]])
