""" O(mn), 106 ms (beats 81.08%), 16.31 MB (beats 96.93%) """


def solve(word1: str, word2: str) -> int:
    if len(word1) > len(word2):
        word1, word2 = word2, word1

    n = len(word1)
    m = len(word2)

    cache = [0] * (n+1)

    for i in range(1, n+1):
        cache[i] = i

    for j in range(1, m+1):
        prev1 = cache[0]
        cache[0] = j

        for i in range(1, n+1):
            prev0 = cache[i]

            if word1[i-1] == word2[j-1]:
                cache[i] = prev1
            else:
                ans_insert = 1+prev0
                ans_remove = 1+cache[i-1]
                ans_replace = 1+prev1

                cache[i] = min(ans_insert, ans_remove, ans_replace)

            prev1 = prev0

    return cache[-1]


if __name__ == "__main__":

    def test(input, expect):
        found = solve(*input)
        assert found == expect, f"expect: {expect}, however found: {found}"

    test(("sea", "eat"), 2)
    test(("horse", "ros"), 3)
    test(("intention", "execution"), 5)
