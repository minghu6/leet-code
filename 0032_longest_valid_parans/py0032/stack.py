from typing import List


def solve(s: str) -> int:
    stack = [-1]  # 保存两个信息，记录连续信息
    ans = 0

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()

            if stack:
                ans = max(ans, i - stack[-1])
            else:
                stack.append(i)

    return ans


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(")()())", 4)
    test("(()(((()", 2)
    test("()(()", 2)
    test("(()", 2)
    test("", 0)
