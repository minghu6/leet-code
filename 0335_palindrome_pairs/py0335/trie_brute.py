""" O(nw^2) """

from typing import List, Optional, MutableMapping
from dataclasses import dataclass, field
from collections import defaultdict

def solve(words: List[str]) -> List[List[int]]:
    trie = PostfixTrie()

    for i, word in enumerate(words):
        trie.add_word(i, word)

    ans = []

    for i, word in enumerate(words):
        pairs = trie.search_palindrome_pairs(i, word)

        ans.extend(pairs)

    return ans


class PostfixTrie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def add_word(self, word_i: int, word: str):
        root = self.root

        if is_palindrome(word):
            root.rest_palindromes.append(word_i)

        for i in reversed(range(0, len(word))):
            cv = IDX[word[i]]

            if root.children.get(cv) is None:
                root.children[cv] = TrieNode()

            root: TrieNode = root.children[cv]

            if is_palindrome(word[:i]):
                root.rest_palindromes.append(word_i)

        root.word_index = word_i

    def search_palindrome_pairs(
        self,
        word_i: int,
        word: str
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

            if root.word_index is not None and is_palindrome(word[i:]):
                pairs.append([word_i, root.word_index])

            if root.children.get(idx) is None:
                break

            root: TrieNode = root.children[idx]
            i += 1


        return pairs


class TrieNode:
    pass


class TrieNode:
    def __init__(self) -> None:
        self.word_index: Optional[int] = None
        self.rest_palindromes: List[int] = []
        self.children: MutableMapping[int, TrieNode] = {}


BASE = ord('a')

IDX = {}

for i in range(0, 26):
    IDX[chr(BASE + i)] = i


def is_palindrome(s: str) -> bool:
    return s and s == s[::-1]


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
