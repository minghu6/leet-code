use std::collections::HashMap;

pub fn solve(mut intervals: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
    intervals.sort_unstable();

    let mut queries: Vec<(i32, usize)> = queries
        .into_iter()
        .enumerate()
        .map(|(i, x)| (x, i))
        .collect();

    queries.sort_unstable();

    let mut data: Vec<i32> = queries
        .iter()
        .map(|x| x.0)
        .chain(intervals.iter().map(|v| v[1]))
        .collect();

    data.sort_unstable();
    data.dedup();

    let data_map: HashMap<i32, usize> = data
        .iter()
        .cloned()
        .enumerate()
        .map(|(i, x)| (x, i))
        .collect();

    let mut bit = FakeBIT::new(data_map.len());

    let mut ans = vec![0; queries.len()];

    let mut prev_q_raw = 0;
    let mut prev_ans = 0;
    let mut i = 0;

    for (q_raw, q_idx) in queries {
        if prev_q_raw == q_raw {
            ans[q_idx] = prev_ans;

            continue;
        }

        let q = *data_map.get(&q_raw).unwrap();

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

            bit.add(*data_map.get(&r).unwrap(), q, r - l + 1);
        }

        let suffix = bit.suffix(q);
        let res = if suffix > 0 { suffix } else { -1 };

        ans[q_idx] = res;

        prev_q_raw = q_raw;
        prev_ans = res;
    }

    ans
}

macro_rules! combine {
    ($inplace: expr, $val:expr) => {
        if $val > 0 && (*$inplace == 0 || $val < *$inplace) {
            *$inplace = $val;
        }
    };
}

macro_rules! range {
    ($i:ident) => {
        ((($i + 1) as isize) & -(($i + 1) as isize)) as usize
    };
}

struct FakeBIT {
    data: Vec<i32>,
}

impl FakeBIT {
    fn new(range_end: usize) -> Self {
        Self {
            data: vec![0; range_end],
        }
    }

    fn add(&mut self, mut i: usize, end: usize, addend: i32) {
        loop {
            combine!(&mut self.data[i], addend);

            if i < range!(i) || i < end {
                break;
            }

            i -= range!(i);
        }
    }

    /// query i
    fn suffix(&self, mut i: usize) -> i32 {
        let mut acc = 0;

        while i < self.data.len() {
            combine!(&mut acc, self.data[i]);

            i += range!(i);
        }

        acc
    }
}


#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn test_bit() {
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
    }
}
