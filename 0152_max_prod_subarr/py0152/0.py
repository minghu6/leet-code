""" 76 ms (beats 78.56%, ~100%), 16.2 MB (beats 99.98%) """

from typing import List
from functools import reduce
from operator import mul


def solve(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    neg = []
    zero = -1

    ans = 0
    nums.append(0)

    for i in range(len(nums)):
        if nums[i] < 0:
            if len(neg) == 2:
                neg[-1] = i
            else:
                neg.append(i)

        elif nums[i] == 0:
            if i-zero < 2:
                cand = 0
            elif i-zero == 2:
                cand = nums[i-1]
            else: #  i-zero > 2
                if len(neg) % 2 == 0:
                    cand = reduce(mul, nums[zero+1:i])
                elif len(neg) == 1:
                    if nums[zero+1:neg[0]]:
                        cand1 = reduce(mul, nums[zero+1:neg[0]])
                    else:
                        cand1 = 0

                    if nums[neg[0]+1:i]:
                        cand2 = reduce(mul, nums[neg[0]+1:i])
                    else:
                        cand2 = 0

                    cand = max(cand1, cand2)
                else:
                    cand1 = reduce(mul, nums[zero+1:neg[-1]])
                    cand2 = reduce(mul, nums[neg[0]+1:i])
                    cand = max(cand1, cand2)

            zero = i
            neg.clear()

            if ans < cand:
                ans = cand

    return ans



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test()
