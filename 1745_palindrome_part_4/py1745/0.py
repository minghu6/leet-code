""" 1892 ms (beats 87.50%), 16.48 MB (beats 54.17%) """


def solve(s: str) -> bool:
    n = len(s)

    p = [[True] * (n-i+1) for i in range(n)]

    for span in range(2, n+1):
        for i in range(n-span+1):
            p[i][span] = p[i+1][span-2] and s[i] == s[i+span-1]

    for i in range(n-2):
        if p[0][i+1]:
            for j in range(i+1, n-1):
                if p[i+1][j-i] and p[j+1][n-1-j]:
                    return True

    return False


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test("abcbdd", True)
    test("bcbddxy", False)
