from typing import List, Optional, MutableMapping


def solve(words: List[str]) -> List[List[int]]:
    # reversed str's prefix
    rev_postfixs: MutableMapping[str, Optional[List[int]]] = {}
    rev_words: MutableMapping[str, int] = {}

    for i, word in enumerate(words):
        rev_word = word[::-1]

        rev_words[rev_word] = i

        for j in range(0, len(rev_word)):
            if is_palindrome(rev_word[j:]):
                if rev_postfixs.get(rev_word[:j]) is None:
                    rev_postfixs[rev_word[:j]] = [i]
                else:
                    rev_postfixs[rev_word[:j]].append(i)

    ans = []

    for i, word in enumerate(words):
        for j in range(-1, len(word)):
            if rev_words.get(word[:j+1]) is not None and is_palindrome(word[j+1:]):
                ans.append([i, rev_words[word[:j+1]]])

            if j == len(word) - 1:
                if rev_words.get(word) is not None and rev_words[word] != i:
                    ans.append([i, rev_words[word]])

                ans.extend([[i, k] for k in rev_postfixs.get(word, [])])

    return ans


def is_palindrome(s: str) -> bool:
    return s and s == s[::-1]


if __name__ == '__main__':
    def test(input, expect):
        found = solve(input)

        expect.sort()
        found.sort()

        assert expect == found, f"expect: {expect}, however found: {found}"

    test(["a", ""], [[0, 1], [1, 0]])
    test(["abcd", "dcba", "lls", "s", "sssll"],
         [[0, 1], [1, 0], [3, 2], [2, 4]])
    test(["bat", "tab", "cat"], [[0, 1], [1, 0]])
