""" O(n) """

from typing import List


def solve(s: str) -> str:
    if not s:
        return 'a'

    return patch(s, max_prefix_palindrome(s))


patch = lambda s, l: ''.join(reversed(s[l:])) + s


def max_prefix_palindrome(s: str) -> int:
    s1 = s + '#' + ''.join(reversed(s))

    pi1 = compute_kmp_prefix_array(s1)

    return pi1[-1]


def compute_kmp_prefix_array(s: str) -> List[int]:
    n = len(s)
    pi = [0] * n

    for i in range(1, n):
        pi0 = pi[i-1]

        while True:  # do-while
            if s[i] == s[pi0]:
                pi[i] = pi0 + 1
                break
            if pi0 == 0:
                break
            pi0 = pi[pi0-1]


    return pi



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test("ababbbabbaba", "ababbabbbababbbabbaba")
    test("aacecaaa", "aaacecaaa")
    test("abcd", "dcbabcd")

