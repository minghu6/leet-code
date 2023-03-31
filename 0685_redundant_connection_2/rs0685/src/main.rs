
mod solution_raw;
mod solution_better;

use solution_raw::resolve_raw;
use solution_better::resolve_better;


fn main() {
    let sample = vec![
        (vec![[1, 2], [1, 3], [2, 3]], [2, 3]),
        (vec![[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]], [4, 1]),
        (vec![[2,1],[3,1],[4,2],[1,4]], [2, 1]),
        (vec![[1,2],[2,1],[2,3],[3,4]], [2, 1])
        ];

    let norm_sample = Vec::from_iter(sample
    .into_iter()
    .map(|(input, expect)|
        (
            input
            .into_iter()
            .map(|arr| Vec::from_iter(arr.into_iter()))
            .collect::<Vec<Vec<i32>>>(),

            Vec::from_iter(
                expect
                .into_iter()
            )
        )
    ));

    for (edges, expect) in norm_sample {
        assert_eq!(resolve_raw(edges.clone()), expect,);
        assert_eq!(resolve_better(edges.clone()), expect,);
    }
}

