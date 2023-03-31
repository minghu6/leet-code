def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums = list(enumerate(nums))
    nums.sort(key=lambda x: x[1])

    n = len(nums)
    for i in range(0, n):
        v = target-nums[i][1]
        if nums[n-1][1] < v:
            continue
        lo = i
        hi = n
        while lo < hi:
            pivot = (hi + lo) // 2 # 2
            pivot_v = nums[pivot][1]

            if pivot_v < v:
                lo = pivot + 1
            elif pivot_v > v:
                hi = pivot
            else:
                return [nums[i][0], nums[pivot][0]]
