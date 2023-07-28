from typing import List



def solve(h: List[int]) -> int:
    mode = True  # enum is a little waste of memory
    k = 0  # peak
    ans = 0

    for i in range(1, len(h)):
        if mode:
            if h[i] > h[i-1]:
                mode = not mode
        else:
            if h[i] < h[i-1]:
                mode = not mode

        if not mode and h[i] >= h[k]:
            ans += sum(map(lambda j: h[k]-h[j], range(k+1, i)))
            k = i

    mode = True
    oldk = k
    k = len(h) - 1

    for i in range(len(h)-2, oldk-1, -1):
        if mode:
            if h[i] > h[i+1]:
                mode = not mode
        else:
            if h[i] < h[i+1]:
                mode = not mode

        if not mode and h[i] >= h[k]:
            ans += sum(map(lambda j: h[k]-h[j], range(i+1, k)))
            k = i

    return ans



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([4,2,3], 1)
    test([4,2,0,3,2,5], 9)
    test([0,1,0,2,1,0,1,3,2,1,2,1], 6)
