from typing import List, Iterable


class Leaf:
    def __len__(self):
        return 2

    def __repr__(self) -> str:
        return '()'


class Branch: pass

class Branch:
    def __init__(self, children: List[Leaf | Branch]) -> None:
        self.children = children
        self.repr = '({})'.format(
            ''.join([repr(child) for child in self.children])
        )
        self.hash = hash(self.repr)

    def __repr__(self) -> str:
        return self.repr

    def __hash__(self):
        return self.hash

    def __eq__(self, other: object) -> bool:
        return repr(self) == repr(other)


leaf = Leaf()
parens = [
    {(leaf,)},
    {(Branch([leaf]),), (leaf, leaf)}
]


def solve(n: int) -> List[str]:
    for i in range(len(parens), n):
        parens.append(set(gen_paren_comb(i-1)))

    return [''.join([repr(part) for part in parts]) for parts in parens[n-1]]


def gen_paren_comb(prev_i: int):
    for parts in parens[prev_i]:
        # nested on each parens units: 1~n
        for k in range(len(parts), 0, -1):
            for j in range(0, len(parts)-k+1):
                yield parts[:j] + (Branch(parts[j:j+k]),) + parts[j+k:]

    yield (leaf,) * (prev_i+2)


if __name__ == '__main__':
    from typing import Iterable
    from collections import Counter

    def duplicated(input: Iterable) -> List:
        d = Counter(input)

        return [e for e in d if d[e] > 1]

    def test(input, expect):
        found = solve(input)
        dup = duplicated(found)

        assert len(found) == len(
            expect), f"{len(found)}/{len(expect)} duplicated: {dup if dup else '<empty>' }"
        assert set(found) == set(
            expect), f"expect: {expect}, however found: {found}"

    # print(solve(3))
    # print(solve(4))

    test(3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
    test(1, ["()"])
    test(4, ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()",
         "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"])
    test(5, ["((((()))))", "(((()())))", "(((())()))", "(((()))())", "(((())))()", "((()(())))", "((()()()))",
             "((()())())", "((()()))()", "((())(()))", "((())()())", "((())())()", "((()))(())", "((()))()()",
             "(()((())))", "(()(()()))", "(()(())())", "(()(()))()", "(()()(()))", "(()()()())", "(()()())()",
             "(()())(())", "(()())()()", "(())((()))", "(())(()())", "(())(())()", "(())()(())", "(())()()()",
             "()(((())))", "()((()()))", "()((())())", "()((()))()", "()(()(()))", "()(()()())", "()(()())()",
             "()(())(())", "()(())()()", "()()((()))", "()()(()())", "()()(())()", "()()()(())", "()()()()()"])
