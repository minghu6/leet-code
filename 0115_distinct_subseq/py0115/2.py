""" 95 ms (beats 92.78%), 16.5 MB (beats 96.74%) """


def solve(s: str, t: str) -> int:
    n = len(s)
    m = len(t)

    if n < m:
        return 0

    rec = [0] * m

    for i in range(n):
        pre = 1

        for j in range(min(i+1, m)):
            tmp = rec[j]

            if s[i] == t[j]:
                rec[j] += pre

            pre = tmp

    return rec[-1]


if __name__ == "__main__":

    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("rabbbit", "rabbit"), 3)
    test(("babgbag", "bag"), 5)
