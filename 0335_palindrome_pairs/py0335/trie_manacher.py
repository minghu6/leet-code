""" O(nw) 8028ms(beats 5.12%), 424.8MB(beats5.36%) """

from typing import List, Iterable, Optional, Tuple
from dataclasses import dataclass, field


def solve(words: List[str]) -> List[List[int]]:
    postfix_tabs = []
    trie = PostfixTrie()

    for i, word in enumerate(words):
        prefix, postfix = prefix_postfix_palindrome_table(word)

        trie.add_word(i, word, prefix)
        postfix_tabs.append(postfix)

    ans = []

    for i, word in enumerate(words):
        pairs = trie.search_palindrome_pairs(i, word, postfix_tabs[i])

        ans.extend(pairs)

    return ans


class PostfixTrie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def add_word(self, word_i: int, word: str, prefix_tab: List[bool]):
        root = self.root

        if prefix_tab and prefix_tab[-1]:
            root.rest_palindromes.append(word_i)

        for i in reversed(range(0, len(word))):
            cv = IDX[word[i]]

            if root.children[cv] is None:
                root.children[cv] = TrieNode()

            root: TrieNode = root.children[cv]

            if i > 0 and prefix_tab[i-1]:
                root.rest_palindromes.append(word_i)

        root.word_index = word_i

    def search_palindrome_pairs(
        self,
        word_i: int,
        word: str,
        postfix_tab: List[bool]
    ) -> List[List[int]]:
        pairs = []
        root = self.root
        i = 0

        while True:
            if i == len(word):
                if root.word_index is not None and word_i != root.word_index:
                    pairs.append([word_i, root.word_index])

                pairs.extend(map(lambda j: [word_i, j], root.rest_palindromes))

                break

            idx = IDX[word[i]]

            if root.word_index is not None and postfix_tab[i]:
                pairs.append([word_i, root.word_index])

            if root.children[idx] is None:
                break

            root: TrieNode = root.children[idx]
            i += 1


        return pairs


class TrieNode:
    pass


@dataclass
class TrieNode:
    word_index: Optional[int] = field(default=None)
    rest_palindromes: List[int] = field(default_factory=lambda: [])
    children: List[Optional[TrieNode]] = field(default_factory=lambda: [None] * 26)


BASE = ord('a')

IDX = {}

for i in range(0, 26):
    IDX[chr(BASE + i)] = i


def prefix_postfix_palindrome_table(s: str) -> Tuple[List[int], List[int]]:
    d1 = compute_d1(s)
    d2 = compute_d2(s)
    n = len(s)

    prefix = [False] * n
    postfix = [False] * n

    for i, r in enumerate(d1):
        rl = i-r+1
        rr = i+r-1

        if rl == 0:
            prefix[rr] = True
        if rr == n-1:
            postfix[rl] = True

    for i, r in enumerate(d2):
        if r == 0:
            continue

        rl = i-r
        rr = i+r-1

        if rl == 0:
            prefix[rr] = True
        if rr == n-1:
            postfix[rl] = True

    return prefix, postfix


def compute_d1(s: str) -> List[int]:
    """ return (i, r) """

    n = len(s)

    d1 = [1] * n

    rl = 0  # rightmost left
    rr = 0  # rightmost right

    for i in range(1, n-1):
        if i < rr:
            j = rr - i + rl

            if d1[j] < j - rl + 1:
                d1[i] = d1[j]
                continue
            else:
                r = j - rl + 1
        else:
            r = 1

        while i+r-1 < n-1 and i-(r-1) > 0 and s[i+r] == s[i-r]:
            r += 1

        if i+r-1 > rr:
            rr = i+r-1
            rl = i-(r-1)

        d1[i] = r

    return d1


def compute_d2(s: str) -> List[int]:
    """ return (i, r) """

    n = len(s)

    d2 = [0] * n

    rl = 0  # rightmost left
    rr = 0  # rightmost right

    for i in range(1, n):
        if i < rr:
            j = rr - i + rl + 1

            if d2[j] < j - rl:
                d2[i] = d2[j]
                continue
            else:
                r = j - rl
        else:
            r = 0

        while i+r-1 < n-1 and i-r > 0 and s[i-r-1] == s[i+r]:
            r += 1

        if i+r-1 > rr:
            rr = i+r-1
            rl = i-r

        d2[i] = r

    return d2


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)

        expect.sort()
        found.sort()

        assert expect == found, f"expect: {expect}, however found: {found}"

    test(["abcd", "dcba", "lls", "s", "sssll"],
         [[0, 1], [1, 0], [3, 2], [2, 4]])
    test(["bat", "tab", "cat"], [[0, 1], [1, 0]])
    test(["a", ""], [[0, 1], [1, 0]])
