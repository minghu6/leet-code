""" O(nlogn) 1072ms beats 42.67% """

from typing import List
from math import log2


def solve(s: str) -> str:
    n = len(s)

    forward_hash = PrefixHash(s)
    backward_hash = PrefixHash(''.join(reversed(s)))

    # Odd

    odd_r = 1
    odd_i = 0

    for i in range(0, n):
        max_r = min(i+1, n-i)

        if max_r <= odd_r:
            continue

        acc_r = 0

        for k in reversed(range(0, int(log2(max_r)) + 1)):
            r = acc_r + 2 ** k

            if r > max_r:
                continue

            if forward_hash.query(i, i+r-1) == backward_hash.query(n-1-i, n-1-i+r-1):
                acc_r = r

        if acc_r > odd_r:
            odd_r = acc_r
            odd_i = i

    # Even

    even_r = 0
    even_i = 1

    for i in range(1, n):
        max_r = min(i, n-i)

        if max_r <= even_r:
            continue

        acc_r = 0

        for k in reversed(range(0, int(log2(max_r)) + 1)):
            r = acc_r + 2 ** k

            if r > max_r:
                continue

            if forward_hash.query(i, i+r-1) == backward_hash.query(n-i, n-i+r-1):
                acc_r = r

        if acc_r > even_r:
            even_r = acc_r
            even_i = i

    if even_r >= odd_r:
        return s[even_i - even_r : even_i+even_r]
    else:
        return s[odd_i - odd_r+1: odd_i+odd_r]



# 对于只数字和英文字符, p=79

P = 79
M = 10 ** 9
N = 1000  # Max String Length

NPOWS = [1] * N

for i in range(1, N):
    NPOWS[i] = NPOWS[i-1] * P % M


# it's nosense both considering correctness and performance
# def rank(c: str):
#     if '0' <= 'c' <= '9':
#         return ord(c) - ord('0') + 1
#     elif 'A' <= 'c' <= 'Z':
#         return ord(c) - ord('A') + 10 + 1
#     else:
#         return ord(c) - ord('a') + 26 + 10 + 1



class PrefixHash:
    def __init__(self, s: str) -> None:
        self.prefix = [0] * len(s)

        self.build_prefix(self.prefix, s)

    @staticmethod
    def build_prefix(l: List[int], s: str):
        if not s:
            return

        l[0] = ord(s[0])

        for i in range(1, len(s)):
            l[i] = (l[i-1] * P % M + ord(s[i])) % M

    def query(self, l: int, r: int) -> int:
        """ [l, r] """

        a = self.prefix[r]
        b = self.prefix[l-1] * NPOWS[r-(l-1)] % M if l > 0 else 0

        return (a + M - b) % M





if __name__ == '__main__':
    def test(input, expect):
        assert solve(input) == expect

    test('ccc', 'ccc')
    test('babad', 'bab')
    test('cbbd', 'bb')
    test('a', 'a')

