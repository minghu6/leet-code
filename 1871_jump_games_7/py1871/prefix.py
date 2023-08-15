""" O(n) 173 ms (beats 97.52%), 21.07 MB (beats 25.62) """

from itertools import islice

def solve(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)

    if s[-1] != '0':
        return False

    if n <= maxJump+1:
        return True

    prefix = [1] * n

    it = enumerate(s)

    for i, v in islice(it, minJump, maxJump+1):
        prefix[i] = prefix[i-1]

        if v == '0':
            prefix[i] += 1

    for i, v in it:
        prefix[i] = prefix[i-1]

        if v == '0' and prefix[i-minJump] - prefix[i-maxJump-1]:
            prefix[i] += 1

    return prefix[-1] - prefix[-2] == 1


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("0000000000", 8, 8), False)
    test(("011010", 2, 3), True)
    test(("01101110", 2, 3), False)

