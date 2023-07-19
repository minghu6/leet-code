""" 1468 ms (beats 53.24%), 40.78 mb (beats 38.31%, ~100%) """

from typing import List
from collections import Counter

BASE = ord('a')

def solve(words: List[str]) -> int:
    counter = Counter(words)

    n = 0
    has_odd_sym = False

    for i in range(0, 26):
        n += counter[chr(i+BASE) * 2] // 2

        if not has_odd_sym and counter[chr(i+BASE) * 2] % 2 > 0:
            has_odd_sym = True

        n += sum(
            map(
                lambda j: min(counter[chr(i+BASE)+chr(j+BASE)], counter[chr(j+BASE)+chr(i+BASE)]),
                range(i+1, 26)
            ))

    return ((n * 2 + 1) if has_odd_sym else n * 2) * 2



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(["lc","cl","gg"], 6)
    test(["ab","ty","yt","lc","cl","ab"], 8)
    test(["cc","ll","xx"], 2)
