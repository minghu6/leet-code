
from itertools import chain
from typing import List


def palindromePairs(self, words: List[str]) -> List[List[int]]:

    words = sorted(chain(((i, w, False) for i, w in enumerate(words)),
                            ((i, w[::-1], True) for i, w in enumerate(words))),
                            key=lambda x: x[1])

    for i, (idx1, w1, is_reversed1) in enumerate(words):
        for j in range(i + 1, len(words)):
            idx2, w2, is_reversed2 = words[j]
            if w2.startswith(w1):
                if is_reversed1 == is_reversed2:
                    continue
                rest = w2[len(w1):]
                if idx1 != idx2 and rest == rest[::-1]:
                    yield (idx1, idx2) if is_reversed2 else (idx2, idx1)
            else:
                break
