""" O(n) 218ms(beats 37.91%), 19.9MB(beats 5.3%) """

from typing import List


def solve(s: str) -> str:
    return patch(s, max_prefix_palindrome(s))


patch = lambda s, l: ''.join(reversed(s[l:])) + s

def max_prefix_palindrome(s: str) -> int:
    d1 = compute_d1(s)
    d2 = compute_d2(s)

    odd_r = 1

    for i, r in enumerate(d1):
        if i+1 == r and r > odd_r:
            odd_r = r

    even_r = 0

    for i, r in enumerate(d2):
        if i == r and r > even_r:
            even_r = r

    return max(odd_r*2-1, even_r*2)


def compute_d1(s: str) -> List[int]:
    """ return (i, r) """

    n = len(s)

    d1 = [1] * n

    rl = 0  # rightmost left
    rr = 0  # rightmost right

    for i in range(1, n-1):
        if i < rr:
            j = rr - i + rl

            if d1[j] < j - rl + 1:
                d1[i] = d1[j]
                continue
            else:
                r = j - rl + 1
        else:
            r = 1

        while i+r-1 < n-1 and i-(r-1) > 0 and s[i+r] == s[i-r]:
            r += 1

        if i+r-1 > rr:
            rr = i+r-1
            rl = i-(r-1)

        d1[i] = r

    return d1


def compute_d2(s: str) -> List[int]:
    """ return (i, r) """

    n = len(s)

    d2 = [0] * n

    rl = 0  # rightmost left
    rr = 0  # rightmost right

    for i in range(1, n):
        if i < rr:
            j = rr - i + rl + 1

            if d2[j] < j - rl:
                d2[i] = d2[j]
                continue
            else:
                r = j - rl
        else:
            r = 0

        while i+r-1 < n-1 and i-r > 0 and s[i-r-1] == s[i+r]:
            r += 1

        if i+r-1 > rr:
            rr = i+r-1
            rl = i-r

        d2[i] = r

    return d2



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test("aacecaaa", "aaacecaaa")
    test("abcd", "dcbabcd")
