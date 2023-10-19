""" 183 ms (beats 95.32%), 16.34 MB (beats 92.92%) """

from typing import List


def solve(nums1: List[int], nums2: List[int]) -> int:
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1

    n = len(nums1)
    m = len(nums2)

    # if nums1[0] * nums2[0] < 0\
    # and all(map(lambda x: x * nums1[0] > 0, nums1[1:]))\
    # and all(map(lambda x: x * nums2[0] > 0, nums2[1:])):
    #     return -min(map(lambda x:abs(x), nums1)) * min(map(lambda x:abs(x), nums2))

    nums1_max = max(nums1)
    nums2_min = min(nums2)

    if nums1_max < 0 and nums2_min > 0:
        return nums1_max * nums2_min

    nums1_min = min(nums1)
    nums2_max = max(nums2)

    if nums1_min > 0 and nums2_max < 0:
        return nums1_min * nums2_max

    cache = [0] * m

    for i in range(n):
        pre1 = cache[0]
        cache[0] = max(nums1[i]*nums2[0], cache[0])

        for j in range(1, m):
            pre0 = cache[j]

            cache[j] = max(
                pre0,
                cache[j-1],
                nums1[i]*nums2[j]+pre1,
                nums1[i]*nums2[j]
            )

            pre1 = pre0

    return cache[m-1]


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([3,-1,0], [4,5,3]), 15)
    test(([-3,-8,3,-10,1,3,9], [9,2,3,7,-9,1,-8,5,-1,-1]), 200)
    test(([3,-2], [2,-6,7]), 21)
    test(([-5,-1,-2], [3,3,5,5]), -3)
    test(([2,1,-2,5], [3,0,-6]), 18)
    test(([-1,-1], [1,1]), -1)
