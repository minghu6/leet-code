""" O(n^2) 164 ms (beats 74.64%), 17.6 MB (beats 98.33%) """

from typing import List
from collections import defaultdict


def solve(stones: List[int]) -> bool:
    if stones[1] != 1:
        return False

    if len(stones) == 2:
        return True

    k_candicates = defaultdict(set, {1: [1]})

    for v in stones[1:-1]:
        for k in k_candicates.pop(v, []):
            if abs(v+k-stones[-1]) <= 1:
                return True

            if k > 1:
                k_candicates[v+k-1].add(k-1)
            k_candicates[v+k].add(k)
            k_candicates[v+k+1].add(k+1)

    return False


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([0,2], False)
    test([0,1,3,5,6,8,12,17], True)
    test([0,1,2,3,4,8,9,11], False)
