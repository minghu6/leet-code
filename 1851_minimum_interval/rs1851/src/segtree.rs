use std::{
    cmp::{max, min},
    collections::HashMap,
};

pub fn solve(intervals: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
    let mut data: Vec<i32> = intervals
        .iter()
        .cloned()
        .flatten()
        .chain(queries.iter().cloned())
        .collect();

    data.sort_unstable();
    data.dedup();

    let data_map: HashMap<i32, usize> = data
        .iter()
        .cloned()
        .enumerate()
        .map(|(i, x)| (x, i))
        .collect();

    let mut tree = SegmentTree::new(data_map.len());

    for interval in intervals {
        let l = interval[0];
        let r = interval[1];

        let val = r - l + 1;
        let l = *data_map.get(&l).unwrap();
        let r = *data_map.get(&r).unwrap();

        tree.update(l, r, val);
    }

    let mut ans = Vec::with_capacity(queries.len());

    for q in queries {
        let i = data.binary_search(&q).unwrap();

        let res = tree.query(i, i);

        if res == 0 {
            ans.push(-1);
        } else {
            ans.push(res);
        }
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

/// DFS 型
struct SegmentTree {
    /// range update
    data: Vec<i32>,
    range_end: usize,
}

impl SegmentTree {
    fn new(range_end: usize) -> Self {
        Self {
            data: vec![0; range_end * 2],
            range_end,
        }
    }

    fn update(&mut self, l: usize, r: usize, val: i32) {
        self.update_(l, r, 0, self.range_end - 1, 0, val)
    }

    fn update_(&mut self, l: usize, r: usize, tl: usize, tr: usize, i: usize, val: i32) {
        if l > r {
            return;
        }

        if l == tl && r == tr {
            combine!(&mut self.data[i], val);
        } else {
            let mid = (tl + tr) / 2;
            let sub_len = mid - tl + 1;

            let i_lf = i + 1;
            let i_rh = i + 2 * sub_len;

            combine!(&mut self.data[i_lf], self.data[i]);
            combine!(&mut self.data[i_rh], self.data[i]);

            self.update_(l, min(mid, r), tl, mid, i_lf, val);
            self.update_(max(l, mid + 1), r, mid + 1, tr, i_rh, val);
        }
    }

    fn query(&mut self, l: usize, r: usize) -> i32 {
        self.query_(l, r, 0, self.range_end - 1, 0)
    }

    fn query_(&mut self, l: usize, r: usize, tl: usize, tr: usize, i: usize) -> i32 {
        if l > r {
            return 0;
        }

        if l == tl && r == tr {
            self.data[i]
        } else {
            let mid = (tl + tr) / 2;
            let sub_len = mid - tl + 1;

            let i_lf = i + 1;
            let i_rh = i + 2 * sub_len;

            combine!(&mut self.data[i_lf], self.data[i]);
            combine!(&mut self.data[i_rh], self.data[i]);

            let lv = self.query_(l, min(mid, r), tl, mid, i_lf);
            let rv = self.query_(max(l, mid + 1), r, mid + 1, tr, i_rh);

            if lv == 0 {
                rv
            } else if rv == 0 {
                lv
            } else {
                min(lv, rv)
            }
        }
    }
}



#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn test_segtree() {
        assert_eq!(
            solve(
                vec![vec![4, 5], vec![5, 8], vec![1, 9], vec![8, 10], vec![1, 6]],
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
