""" 249 ms (beats 98.79%), 23.6 mb (beats 47.8%) """

from typing import List


def solve(arr: List[int], start: int) -> bool:
    """ false: unvisited, true: visited """

    n = len(arr)
    stack = [start]
    cache = [False] * n

    while stack:
        i = stack.pop()

        if arr[i] == 0:
            return True

        if not cache[i]:
            cache[i] = True

            if i+arr[i] < n:
                stack.append(i+arr[i])
            if i-arr[i] >= 0:
                stack.append(i-arr[i])

    return False



if __name__ == '__main__':
    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(([4,2,3,0,3,1,2], 5), True)
    test(([4,2,3,0,3,1,2], 0), True)
    test(([3,0,2,1,2], 2), False)
