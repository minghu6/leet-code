from typing import List


def solve(s: str) -> int:
    open = 0
    close = 0
    start = -1
    ans = 0

    for i, c in enumerate(s):
        if c == '(':
            if open == close:
                start = i
            open += 1
        elif c == ')':
            close += 1

            if close > open:
                # reset
                open = 0
                close = 0
            elif close == open:
                ans = max(ans, open*2)

    if open > close:
        rev_open = 0
        rev_close = 0
        rev_ans = 0

        for c in s[start+1:][::-1]:
            if c == ')':
                rev_open += 1
            elif c == '(':
                rev_close += 1

                if rev_close > rev_open:
                    # reset
                    rev_open = 0
                    rev_close = 0
                elif rev_close == rev_open:
                    rev_ans = max(rev_ans, rev_open*2)

        ans = max(ans, rev_ans)

    return ans



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test("(()(((()", 2)
    test("()(()", 2)
    test("(()", 2)
    test(")()())", 4)
    test("", 0)
