""" O(n) 826ms (Beats 80.95%), 30.50mb (Beats 52.38%) """

from typing import List


def solve(nums: List[int], k: int) -> int:
    init = nums[0]

    nums = nums[1:]
    n = len(nums)

    cache = [0] * k
    prev_postfix_max = [0] * k
    cur_prefix_max = [0] * k

    blk_rem = n % k
    max_blks = n // k + (1 if blk_rem else 0)

    acc = 0

    for i, v in enumerate(nums[:k]):
        cache[i] = v + acc

        if v > 0:
            acc += v

    for blk in range(1, max_blks):
        prev_postfix_max[k-1] = cache[k-1]

        for j in range(k-2, -1, -1):
            prev_postfix_max[j] = max(prev_postfix_max[j+1], cache[j])

        cur_prefix_max[0] = cache[0] = prev_postfix_max[0] + nums[blk*k]

        if blk == max_blks-1 and blk_rem:
            tail = blk_rem
        else:
            tail = k

        for j in range(1, tail):
            cache[j] = max(prev_postfix_max[j], cur_prefix_max[j-1]) + nums[blk*k+j]
            cur_prefix_max[j] = max(cur_prefix_max[j-1], cache[j])

    return init + cache[(k+blk_rem-1) % k]



if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([100,-1,-100,-1,100], 2), 198)
    test(([1,-1,-2,4,-7,3], 2), 7)
    test(([10,-5,-2,4,0,3], 3), 17)
    test(([1,-5,-20,4,-1,3,-6,-3], 2), 0)
