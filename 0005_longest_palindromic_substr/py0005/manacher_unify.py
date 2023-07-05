""" O(n) 138ms, beats 96.32%"""

from typing import List


def solve(s: str) -> str:
    if len(s) == 1:
        return s

    s1 = '#'.join(s)
    d1_1 = compute_d1(s1)

    (odd_i1, odd_r1) = max(
        filter(lambda x: x[0] % 2 == 0, enumerate(d1_1)),
        key=lambda x: x[1])

    (even_i1, even_r1) = max(
        filter(lambda x: x[0] % 2 > 0, enumerate(d1_1)),
        key=lambda x: x[1])

    odd_i = odd_i1 // 2
    odd_r = (odd_r1+1) // 2

    even_i = (even_i1+1) // 2
    even_r = even_r1 // 2

    if even_r >= odd_r:
        return s[even_i-even_r: even_i+even_r]
    else:
        return s[odd_i-odd_r+1: odd_i+odd_r]


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


if __name__ == '__main__':
    def test(input, expect):
        if isinstance(expect, str):
            expect = [expect]

        found = solve(input)
        assert found in expect, f"expect one of: {expect}, however found: {found}"

    test('abb', 'bb')
    test('ccc', 'ccc')
    test('babad', ['bab', 'aba'])
    test('cbbd', 'bb')
    test('a', 'a')
