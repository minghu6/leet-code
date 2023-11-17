""" 73 ms (beats 88.24%, ~100%), 16.95 MB (~100%) """


from typing import List


def solve(nums: List[int]) -> int:
    pos = neg = None
    ans = nums[0]

    for v in nums:
        if v > 0:
            if pos is not None:
                pos *= v
            else:
                pos = v

            if neg is not None:
                neg *= v

            if pos > ans:
                ans = pos
        elif v == 0:
            if ans < 0:
                ans = 0
            pos = neg = None
        else:
            if neg is None:
                if pos is None:
                    neg = v
                else:
                    pos, neg = None, pos * v
            else:
                if pos is None:
                    pos, neg = neg * v, v
                else:
                    pos, neg = neg * v, pos * v

                if pos > ans:
                    ans = pos

    return ans
