""" Unify 189 ms (beats 95.32%), 16.29 MB (beats 97.06%, ~100%) """


from typing import List


def solve(nums1: List[int], nums2: List[int]) -> int:
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1

    n = len(nums1)
    m = len(nums2)

    cache = [0] * m
    cache[0] = nums1[0]*nums2[0]

    for j in range(1, m):
        cache[j] = max(nums1[0]*nums2[j], cache[j-1])

    for i in range(1, n):
        pre1 = cache[0]
        cache[0] = max(nums1[i]*nums2[0], cache[0])

        for j in range(1, m):
            pre0 = cache[j]

            cache[j] = max(
                pre0,
                cache[j-1],
                nums1[i]*nums2[j],
                nums1[i]*nums2[j]+pre1,
            )

            pre1 = pre0

    return cache[m-1]
