"""O(n^2) 448ms, beats 92.33%"""

def solve(s: str) -> str:
    n = len(s)

    # Odd symmetric

    ans_odd_r = 0
    ans_odd_i = 0

    for i in range(1, n-1):
        max_len = min(i, n-1-i)

        r = 0

        for l in range(1, max_len + 1):
            if s[i-l] == s[i+l]:
                r += 1
            else:
                break

        if r > ans_odd_r:
            ans_odd_r = r
            ans_odd_i = i

    # Even symmetric

    ans_even_r = 0
    ans_even_i = 0

    for i in range(0, n-1):
        max_len = min(i+1, n-1-i)

        r = 0

        for l in range(1, max_len+1):
            if s[i -(l - 1)] == s[i + l]:
                r += 1
            else:
                break

        if r > ans_even_r:
            ans_even_r = r
            ans_even_i = i

    if ans_odd_r >= ans_even_r:
        return s[ans_odd_i - ans_odd_r : ans_odd_i + ans_odd_r + 1]
    else:
        return s[ans_even_i - (ans_even_r - 1) : ans_even_i + ans_even_r + 1]



if __name__ == '__main__':
    def test(input, expect):
        assert solve(input) == expect

    test('ccc', 'ccc')
    test('babad', 'bab')
    test('cbbd', 'bb')
    test('a', 'a')

