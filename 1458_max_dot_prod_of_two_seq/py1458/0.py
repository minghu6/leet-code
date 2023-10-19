""" 282 ms (beats 82.09%), 19.02 MB (beats 66.24%) """

from typing import List


def solve(nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    m = len(nums2)

    if nums1[0] * nums2[0] < 0\
    and all(map(lambda x: x * nums1[0] > 0, nums1[1:]))\
    and all(map(lambda x: x * nums2[0] > 0, nums2[1:])):
        return -min(map(lambda x:abs(x), nums1)) * min(map(lambda x:abs(x), nums2))

    cache = [[0] * m for _ in range(n)]

    cache[0][0] = max(0, nums1[0]*nums2[0])

    for j in range(1, m):
        cache[0][j] = max(nums1[0]*nums2[j], cache[0][j-1])

    for i in range(1, n):
        cache[i][0] = max(nums1[i]*nums2[0], cache[i-1][0])

        for j in range(1, m):
            cache[i][j] = max(
                cache[i-1][j],
                cache[i][j-1]
            )

            if nums1[i]*nums2[j]+cache[i-1][j-1] > cache[i][j] :
                cache[i][j] = nums1[i]*nums2[j]+cache[i-1][j-1]

    return cache[n-1][m-1]


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([-3,-8,3,-10,1,3,9], [9,2,3,7,-9,1,-8,5,-1,-1]), 200)
    test(([3,-2], [2,-6,7]), 21)
    test(([-5,-1,-2], [3,3,5,5]), -3)
    test(([2,1,-2,5], [3,0,-6]), 18)
    test(([-1,-1], [1,1]), -1)
