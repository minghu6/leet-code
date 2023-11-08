""" 548 ms (beats 97.84%), 16.28 MB (beats 95.08%) """

from math import inf

def solve(s: str) -> int:
    n = len(s)

    # -> 161 ms
    #

    if s == s[::-1]:
        return 0

    for i in range(1, n):
        if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
            return 1

    cache = [0] * (n+1)
    p = [True] * n

    for i in range(n):
        ans = inf

        for j in range(i+1):
            if s[j] == s[i] and (i-j < 2 or p[j+1]):
                p[j] = True

                if cache[j-1] < ans:
                    ans = cache[j-1]
            else:
                p[j] = False

        cache[i] = ans + 1

    return cache[n-1] - 1
