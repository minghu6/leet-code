from collections import Counter

def solve(s1: str, s2: str, s3: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)

    if n1 + n2 != n3:
        return False

    if Counter(s1) + Counter(s2) != Counter(s3):
        return False

    mem = [False] * (n2 + 1)
    mem[0] = True

    for j in range(1, n2 + 1):
        if s2[j-1] == s3[j-1]:
            mem[j] = True
        else:
            break

    for i in range(1, n1 + 1):
        if not mem[0] or s1[i - 1] != s3[i - 1]:
            mem[0] = False

        for j in range(1, n2 + 1):
            if (
                mem[j]
                and s1[i - 1] == s3[i + j - 1]
                or mem[j - 1]
                and s2[j - 1] == s3[i + j - 1]
            ):
                mem[j] = True
            else:
                mem[j] = False

    return mem[n2]


if __name__ == "__main__":

    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("ab", "bc", "bbac"), False)
    test(("aabcc", "dbbca", "aadbbcbcac"), True)
    test(("aabcc", "dbbca", "aadbbbaccc"), False)
    test(("", "", ""), True)
