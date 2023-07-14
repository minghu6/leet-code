from typing import List


def solve(words: List[str]) -> List[List[int]]:
    ans = []

    for i in range(0, len(words)):
        for j in range(i+1, len(words)):
            x = i
            y = j
            word_x = words[x]
            word_y = words[y]

            if len(word_x) < len(word_y):
                word_x, word_y = word_y, word_x
                x, y = y, x

            rev_y = word_y[::-1]

            if word_x[:len(word_y)] == rev_y \
                and is_palindrome_or_empty(word_x[len(word_y):]):

                ans.append([x, y])

            if rev_y == word_x[len(word_x)-len(word_y):] \
                and is_palindrome_or_empty(word_x[:len(word_x) - len(word_y)]):

                ans.append([y, x])

    return ans


def is_palindrome_or_empty(s: str) -> bool:
    return not s or s == s[::-1]


if __name__ == '__main__':
    def test(input, expect):
        found = list(solve(input))

        expect.sort()
        found.sort()

        assert expect == found, f"expect: {expect}, however found: {found}"

    test(["a","abc","aba",""], [[0,3],[3,0],[2,3],[3,2]])
    test(["abcd", "dcba", "lls", "s", "sssll"],
         [[0, 1], [1, 0], [3, 2], [2, 4]])
    test(["bat", "tab", "cat"], [[0, 1], [1, 0]])
    test(["a", ""], [[0, 1], [1, 0]])
