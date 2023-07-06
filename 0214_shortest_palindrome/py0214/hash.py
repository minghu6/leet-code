""" O(n) 178ms(beats 38.4%), 22.7MB(beats 5.3%) """

from typing import List


def solve(s: str) -> str:
    if not s:
        return 'a'

    return patch(s, max_prefix_palindrome(s))


patch = lambda s, l: ''.join(reversed(s[l:])) + s


def max_prefix_palindrome(s: str) -> int:
    forward_hash = PrefixHash(s)
    backward_hash = PrefixHash(''.join(reversed(s)))

    n = len(s)

    max_l = 1

    for l in reversed(range(2, n+1)):
        if forward_hash.query(0, l-1) == backward_hash.query(n-l, n-1):
            max_l = l
            break

    return max_l


P = 31  # 对于只小写英文字符, p=31
M = 10 ** 9
N = 5 * 10**4  # Max String Length

NPOWS = [1] * N

for i in range(1, N):
    NPOWS[i] = NPOWS[i-1] * P % M

BASE = ord('a')


class PrefixHash:
    def __init__(self, s: str) -> None:
        self.prefix = [0] * len(s)

        self.build_prefix(self.prefix, s)

    @staticmethod
    def build_prefix(l: List[int], s: str):
        if not s:
            return

        l[0] = ord(s[0]) - BASE + 1

        for i in range(1, len(s)):
            l[i] = (l[i-1] * P % M + ord(s[i]) - BASE + 1) % M

    def query(self, l: int, r: int) -> int:
        """ [l, r] """

        a = self.prefix[r]
        b = self.prefix[l-1] * NPOWS[r-(l-1)] % M if l > 0 else 0

        return (a + M - b) % M


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test("aacecaaa", "aaacecaaa")
    test("abcd", "dcbabcd")
