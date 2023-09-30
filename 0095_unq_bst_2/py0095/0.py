"""  ms (beats %),  MB (beats %) """

from typing import List, Optional
from functools import cache
from copy import deepcopy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

@cache
def solve(n: int) -> List[Optional[TreeNode]]:
    """ while saving with range more quick and memory saving though. """

    match n:
        case 0:
            return [None]
        case 1:
            return [TreeNode(1)]
        case _:
            ans = []

            for i in range(n):
                for lf in solve(i):
                    for rh in solve(n-1-i):
                        lf = deepcopy(lf)
                        rh = deepcopy(rh)
                        add(rh, i+1)

                        ans.append(TreeNode(i+1, lf, rh))
            return ans


def add(root, addend: int):
    """ bfs """

    q = [root]

    while q:
        nq = []

        for node in q:
            if node is not None:
                node.val += addend

                nq.append(node.left)
                nq.append(node.right)

        q = nq


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert len(found) == expect, f"expect: {expect}, however found: {len(found)}"

    test(3, 5)
    test(1, 1)
