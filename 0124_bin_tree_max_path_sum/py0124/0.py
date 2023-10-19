""" 79 ms (beats 56.69%, ~100%), 23.83 MB (beats 35.62%) """

from math import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]):
    ans = root.val

    def recur(root: TreeNode):
        if root is None:
            return -inf

        lf = recur(root.left)
        rh = recur(root.right)
        v = max(
            root.val,
            root.val + lf,
            root.val + rh,
        )

        nonlocal ans

        ans = max(
            ans,
            v,
            root.val + lf + rh,
        )

        return v

    recur(root)

    return ans



if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test()
