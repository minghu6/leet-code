from typing import List


def solve(n: int) -> List[str]:
    ans = []

    def build(s: str, open: int, close: int):
        if len(s) ==n * 2:
            ans.append(s)
            return

        if close == open:
            build(s+'(', open+1, close)
        elif open == n:
            build(s+')', open, close+1)
        else:
            build(s+'(', open+1, close)
            build(s+')', open, close+1)

    build("", 0, 0)

    return ans





if __name__ == '__main__':
    from typing import Iterable
    from collections import Counter

    def duplicated(input: Iterable) -> List:
        d = Counter(input)

        return [e for e in d if d[e] > 1]


    def test(input, expect):
        found = solve(input)

        assert len(found) == len(
            expect), f"{len(found)}/{len(expect)} duplicated: {duplicated(found)}"
        assert set(found) == set(
            expect), f"expect: {expect}, however found: {found}"

    test(3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
    test(1, ["()"])
    test(4, ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()",
         "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"])
