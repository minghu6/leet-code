""" O(n) 537 ms (beats 99.80%), 26.77 MB (beats 99.95%) """

from typing import List


def solve(nums: List[int]) -> int:
    ans = acc = nums.pop()

    while nums:
        v = nums.pop()
        tmp = acc + v

        if tmp > v:
            acc = tmp
        else:
            acc = v

        if ans < acc:
            ans = acc

    return ans


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([-2,1,-3,4,-1,2,1,-5,4], 6)
    test([1], 1)
    test([5,4,-1,7,8], 23)
