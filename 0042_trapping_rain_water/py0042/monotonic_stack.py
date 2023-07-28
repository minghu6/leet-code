from typing import List
from itertools import pairwise


def solve(h: List[int]) -> int:
    stack = [0]
    ans = 0

    for i in range(1, len(h)):
        if h[i] > h[stack[-1]]:
            cache = [stack.pop()]

            while stack and h[stack[-1]] <= h[i]:
                cache.append(stack.pop())

            ans += sum(map(lambda k: (h[k[1]]-h[k[0]])*(i-k[1]-1), pairwise(cache)))

            if stack:
               ans += (h[i]-h[cache[-1]])*(i-stack[-1]-1)

        stack.append(i)


    return ans



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([5,5,1,7,1,1,5,2,7,6], 23)
    test([4,2,0,3,2,5], 9)
    test([4,2,3], 1)
    test([0,1,0,2,1,0,1,3,2,1,2,1], 6)
