""" 1281 ms (beats 98.19%), 40.78 MB (beats 38.31%, ~100%) """



from typing import List
from collections import Counter


unique_cases = []

for i in range(0, 25):
    for j in range(i+1, 26):
        unique_cases.append((
            chr(i+ord('a')) + chr(j+ord('a')),
            chr(j+ord('a')) + chr(i+ord('a')),
        ))

common_cases = []

for i in range(0, 26):
    common_cases.append(chr(i+ord('a')) * 2)


def solve(words: List[str]) -> int:
    counter = Counter(words)

    n1 = sum([min(counter[forward], counter[backward]) for forward, backward in unique_cases])
    n2 = sum([counter[double] // 2 for double in common_cases])
    n3 = 1 if any([counter[double] % 2 != 0 for double in common_cases]) else 0

    return ((n1+n2) * 2 + n3) * 2


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(["ab", "ty", "yt", "lc", "cl", "ab"], 8)
    test(["lc", "cl", "gg"], 6)
    test(["cc", "ll", "xx"], 2)
