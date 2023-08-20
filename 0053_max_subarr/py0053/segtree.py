""" O(n) 1067 ms (beats 5.02%), 53.78 MB (beats 6.15%) """

from typing import List

min_value = -10 ** 4 - 1


def solve(nums: List[int]) -> int:
    tree = build(nums)

    return tree[0][-1]

def build(nums: List[int]):
    """ DFS型 """
    n = len(nums)
    data = [None] * (2*n-1)
    _build(data, nums, 0, n-1, 0)

    return data

def _build(data: List, nums: List[int], tl: int, tr: int, i: int):
    """ pref  0 # max prefix sum
        suff  1 # max suffix sum
        sum   2 # all sum
        ans   3 # max range sum
    """

    if tl == tr:
        data[i] = (nums[tl], nums[tl], nums[tl], nums[tl])
        return

    mid = (tl+tr) // 2
    sub_lf = 2*(mid-tl+1) - 1
    i_lf = i+1
    i_rh = i_lf+sub_lf

    _build(data, nums, tl, mid, i_lf)
    _build(data, nums, mid+1, tr, i_rh)

    data_lf = data[i_lf]
    data_rh = data[i_rh]

    data[i] = (
            max(data_lf[0], data_lf[2]+data_rh[0]),
            max(data_rh[1], data_rh[2]+data_lf[1]),
            data_lf[2]+data_rh[2],
            max(data_lf[3], data_rh[3], data_lf[1]+data_rh[0])
        )


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([-2,1,-3,4,-1,2,1,-5,4], 6)
    test([1], 1)
    test([5,4,-1,7,8], 23)
