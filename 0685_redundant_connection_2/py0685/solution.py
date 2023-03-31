
from typing import List

# O(n)
def findRedundantDirectedConnection(edges: List[List[int]]) -> List[int]:
    vmap = {}  # vertice map
    rvmap = {} # recersed vertice map

    from enum import Enum
    class Mode(Enum):
        Ein1 = 1
        Ein2 = 2

    mode = Mode.Ein1
    start = None
    end = None

    # O(E)
    for u,v in edges:
        l = vmap.get(u, [])
        l.append(v)
        vmap[u] = l

        if rvmap.get(v):
            mode = Mode.Ein2
            start = u
            end = v
        else:
            rvmap[v] = u

    if mode is Mode.Ein2:
        def outd(v):
            return len(vmap.get(v, []))
        def ind(v):
            return 0 if rvmap.get(v) is None else 1

        start2 = rvmap[end]

        # print(f'start: {start}, start2: {start2}')

        if start in vmap.get(end, []):
            return [start, end]

        if start2 in vmap.get(end, []):
            return [start2, end]

        if ind(start) == 0 and outd(start) == 1:
            return [start2, end]

        if ind(start2) == 0 and outd(start2) == 1:
            return [start, end]

        # then anyway, use the latter
        return [start, end]

    # Exact one circle structure
    # No upstream
    # Check if its in a circle
    cirset = set()
    exclude = set()

    def is_circle_v(u, visset):
        # if u in exclude:
        #     return False

        nonlocal cirset

        visset.add(u)
        # print(f'visit {u}')
        l = vmap.get(u, [])

        if len(l) == 0:  # Noncircle
            # exclude.add(u)
            return False
        else:
            for v in l:
                if v in visset:
                    cirset = visset
                    return True
            for v in l:
                if is_circle_v(v, visset):
                    return True

            # exclude.add(u)
            return False

    for v in vmap.keys():
        if is_circle_v(v, set()):
            # print(f'break at {v}')
            break

    # print(f'cirset: {cirset}')
    for u,v in reversed(edges):
        if u in cirset and v in cirset:
            return [u, v]



if __name__ == '__main__':

    data = [
        ([4, 1], [[1,2],[2,3],[3,4],[4,1],[1,5]]),
        ([2, 1], [[2,1],[3,1],[4,2],[1,4]]),
        ([4,2], [[4,2],[1,5],[5,2],[5,3],[2,4]]),
        ([5, 2], [[4,2],[1,5],[5,2],[4,3],[4,1]])
    ]

    for output, input in data:
        res = findRedundantDirectedConnection(input)

        if res != output:
            raise f'expect {output} found {res}'

    findRedundantDirectedConnection([[2,3],[3,1],[3,4],[4,2]])
