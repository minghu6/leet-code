""" 2794 ms (beats 35.22%), 16.37 MB (beats 89.42%) """

from math import inf

def solve(s: str) -> int:
    cache = [0]
    n = len(s)

    for i in range(1, n+1):
        ans = inf

        for j in range(i):
            if s[j:i] == s[j:i][::-1]:
                if ans > cache[j]:
                    ans = cache[j]

        cache.append(ans+1)

    return cache[n]-1



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test()
