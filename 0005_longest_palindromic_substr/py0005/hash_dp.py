""" O(n) 251ms beats 95.4% """

from typing import List


def solve(s: str) -> str:
    n = len(s)

    forward_hash = PrefixHash(s)
    backward_hash = PrefixHash(''.join(reversed(s)))

    max_d = 1
    max_i = 0

    prev_d = 1

    for i in range(1, n):
        for d in reversed(range(1, min(i+1, prev_d+2)+1)):
            if forward_hash.query(i-(d-1), i) == backward_hash.query(n-1-i, n-1-i+(d-1)):
                prev_d = d
                break

        if prev_d > max_d:
            max_d = prev_d
            max_i = i


    return s[max_i-(max_d-1): max_i+1]


# Same with hash native

P = 79
M = 10 ** 9
N = 1000  # Max String Length

NPOWS = [1] * N

for i in range(1, N):
    NPOWS[i] = NPOWS[i-1] * P % M


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
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test('ccc', 'ccc')
    test('babad', 'bab')
    test('cbbd', 'bb')
    test('a', 'a')

