""" 94 ms (beats 92.81%), 16.46 MB (beats 96.82%, ~100%) """


def solve(s: str, t: str) -> int:
    if len(s) < len(t):
        return 0

    if set(s) < set(t):
        return 0

    pos = [[] for _ in range(26 * 2)]

    for i, c in enumerate(t):
        key = ord(c) - ord("a") if ord(c) >= ord("a") else ord(c) - ord("A") + 26
        pos[key].append(i + 1)

    rec = [0] * (len(t) + 1)
    # rec[0] = 1

    for c_i, c in enumerate(s):
        pre_v = 1
        pre_i = 0

        key = ord(c) - ord("a") if ord(c) >= ord("a") else ord(c) - ord("A") + 26

        for i in pos[key]:
            if i > c_i+1:
                break

            tmp = rec[i]

            if i - 1 == pre_i:
                rec[i] += pre_v
            else:
                rec[i] += rec[i - 1]

            pre_v = tmp
            pre_i = i

    return rec[-1]

if __name__ == "__main__":

    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("rabbbit", "rabbit"), 3)
    test(("babgbag", "bag"), 5)
