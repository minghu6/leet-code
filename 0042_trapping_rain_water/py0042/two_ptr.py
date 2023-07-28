from typing import List


def solve(h: List[int]) -> int:
    lf = 0
    rh = len(h) - 1
    lf_max = h[lf]
    rh_max = h[rh]
    ans = 0

    while lf < rh:
        if lf_max < rh_max:
            ans += lf_max - h[lf]

            lf += 1
            lf_max = max(lf_max, h[lf])

        else:
            ans += rh_max - h[rh]

            rh -= 1
            rh_max = max(rh_max, h[rh])

    return ans



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test([4,2,3], 1)
    test([4,2,0,3,2,5], 9)
    test([0,1,0,2,1,0,1,3,2,1,2,1], 6)
