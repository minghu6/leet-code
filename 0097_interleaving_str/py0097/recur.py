"""  ms (beats %),  MB (beats %) """

from collections import Counter


def solve(s1: str, s2: str, s3: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)

    if n1+n2 != n3:
        return False

    if Counter(s1) + Counter(s2) != Counter(s3):
        return False

    mem = [[True] * (n2+1) for _ in range(n1+1)]

    def recur(i: int, j: int) -> bool:
        if i+j == n3:
            return True

        if not mem[i][j]:
            return False

        if i < n1 and s1[i] == s3[i+j] and recur(i+1, j):
            return True

        if j < n2 and s2[j] == s3[i+j] and recur(i, j+1):
            return True

        mem[i][j] = False

        return False

    return recur(0, 0)


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("aabcc", "dbbca", "aadbbcbcac"), True)
    test(("aabcc", "dbbca", "aadbbbaccc"), False)
    test(("", "", ""), True)
