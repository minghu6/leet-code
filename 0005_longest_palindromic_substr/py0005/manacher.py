""" O(n) 99ms, beats 98.74% """

from typing import List


def solve(s: str) -> str:
    d1 = compute_d1(s)
    d2 = compute_d2(s)

    (odd_i, odd_r) = map_d(d1)
    (even_i, even_r) = map_d(d2)

    if even_r >= odd_r:
        return s[even_i-even_r : even_i+even_r]
    else:
        return s[odd_i-odd_r+1 : odd_i+odd_r]


map_d = lambda l: max(enumerate(l), key=lambda x: x[1])


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

    test('ccc', 'ccc')
    test('babad', 'bab')
    test('cbbd', 'bb')
    test('a', 'a')
