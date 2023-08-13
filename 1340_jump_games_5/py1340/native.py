""" O(n^2) 4348ms (beats 5.24%), 16.66mb (90.32%) """

from typing import List


def solve(arr: List[int], d: int) -> int:
    n = len(arr)
    forward = [0] * n
    backward = [0] * n

    for i in range(0, n):
        r = 0

        for j in range(i+1, min(i+d+1, n)):
            if arr[i] <= arr[j]:
                break

            r += 1

        forward[i] = r

        r = 0

        for j in range(i-1, max(0, i-d)-1, -1):
            if arr[i] <= arr[j]:
                break

            r += 1

        backward[i] = r

    data = sorted(enumerate(arr), key=lambda x: x[1])

    cache = [1] * n

    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if data[i][1] == data[j][1]:
                continue

            if data[j][0] < data[i][0]:
                if data[i][0] - data[j][0] <= backward[data[i][0]]:
                    cache[i] = max(cache[i], cache[j] + 1)
            else:
                if data[j][0] - data[i][0] <= forward[data[i][0]]:
                    cache[i] = max(cache[i], cache[j] + 1)

    return max(cache)


if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([22,29,52,97,29,75,78,2,92,70,90,12,43,17,97,18,58,100,41,32], 17), 6)
    test(([7, 6, 5, 4, 3, 2, 1], 1), 7)
    test(([3, 3, 3, 3, 3], 3), 1)
    test(([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2), 4)
