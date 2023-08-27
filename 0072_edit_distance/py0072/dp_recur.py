""" 448 ms (beats 5.1 %), 105 MB (beats 5.76 %) """

from functools import cache

@cache
def solve(word1: str, word2: str) -> int:
    if len(word1) > len(word2):
        word1, word2 = word2, word1

    if not word1:
        return len(word2)

    if not word2:
        return len(word1)

    return min(
        # insert char
        1 + solve(word1, word2[1:]),

        # remove char
        1 + solve(word1[1:], word2),

        # replace char
        (0 if word1[0] == word2[0] else 1) + solve(word1[1:], word2[1:])
    )


if __name__ == "__main__":

    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("sea", "eat"), 2)
    test(("horse", "ros"), 3)
    test(("intention", "execution"), 5)
