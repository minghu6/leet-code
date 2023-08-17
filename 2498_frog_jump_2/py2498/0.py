""" O(n) 558 ms (beats 98.8%), 31.12 MB (beats 44.23%) """

from typing import List


def solve(stones: List[int]) -> int:
    n = len(stones)

    if n <= 2:
        return stones[-1]-stones[0]

    # ans = stones[1]-stones[0]

    for i in range(3, n-1, 2):
        ans = max(ans, stones[i]-stones[i-2], stones[i+1]-stones[i-1])

    if (n-1) % 2 == 1:
        ans = max(ans, stones[-1]-stones[-3])

    # for i in range(0, n-2):
    #     ans = max(ans, stones[i+2]-stones[i])

    return ans



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([0,2,5,6,7], 5)
    test([0,3,9], 9)
