""" 44 ms (beats 99.44%, ~100%), 16.29 MB (beats 99.85%, ~100%) """


def solve(s: str, t: str) -> int:
    n = len(s)
    m = len(t)

    if n < m:
        return 0

    rec = [0] * (m+1)
    rec[0] = 1

    for i in range(n-m+1):
        for j in range(m):
            if s[i+j] == t[j]:
                rec[j+1] += rec[j]

    return rec[-1]


if __name__ == "__main__":

    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("rabbbit", "rabbit"), 3)
    test(("babgbag", "bag"), 5)
