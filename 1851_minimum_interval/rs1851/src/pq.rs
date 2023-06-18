use std::{collections::BinaryHeap, cmp::Reverse};


pub fn solve(mut intervals: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
    intervals.sort_unstable_by_key(|v| v[0]);

    let mut queries: Vec<(i32, usize)> = queries
        .into_iter()
        .enumerate()
        .map(|(i, x)| (x, i))
        .collect();

    queries.sort_unstable();

    let mut ans = vec![0; queries.len()];

    let mut prev_q_raw = 0;
    let mut prev_ans = 0;

    let mut i = 0;
    let mut heap = BinaryHeap::new();

    for (q_raw, q_idx) in queries {
        if prev_q_raw == q_raw {
            ans[q_idx] = prev_ans;

            continue;
        }

        while i < intervals.len() {
            let l = intervals[i][0];
            let r = intervals[i][1];

            if l > q_raw {
                break;
            }

            i += 1;

            if r < q_raw {
                continue;
            }

            heap.push(PQE(r, Reverse(r - l + 1)));
        }

        let mut res = -1;

        while let Some(PQE(r, v)) = heap.peek() {
            if *r >= q_raw {
                res = v.0;
                break;
            }

            heap.pop();
        }

        ans[q_idx] = res;

        prev_q_raw = q_raw;
        prev_ans = res;
    }

    ans
}


#[derive(PartialEq, Eq, Ord)]
struct PQE(i32, Reverse<i32>);

impl PartialOrd for PQE {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        self.1.partial_cmp(&other.1)
    }
}


#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn test_pq() {
        assert_eq!(
            solve(
                vec![vec![1, 4], vec![2, 4], vec![3, 6], vec![4, 4]],
                vec![2, 3, 4, 5]
            ),
            vec![3, 3, 1, 4]
        );
        assert_eq!(
            solve(
                vec![vec![2, 3], vec![2, 5], vec![1, 8], vec![20, 25]],
                vec![2, 19, 5, 22]
            ),
            vec![2, -1, 4, 6]
        );
        assert_eq!(
            solve(
                vec![
                    vec![4, 5],
                    vec![5, 8],
                    vec![1, 9],
                    vec![8, 10],
                    vec![1, 6]
                ],
                vec![7, 9, 3, 9, 3]
            ),
            vec![4, 3, 6, 3, 6]
        );
    }
}
