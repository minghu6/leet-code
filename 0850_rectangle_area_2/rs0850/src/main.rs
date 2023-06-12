use std::{
    cmp::{max, min},
    collections::{BTreeSet, HashMap},
};

const M: u64 = 1_000_000_000 + 7;

pub fn solve(rectangles: Vec<Vec<i32>>) -> i32 {
    let (y_data, y_map) = build_y_discrezation(&rectangles);

    let lines = build_x_lines(rectangles, &y_map);

    let mut tree = SegmentTree::new(y_data, y_map.len());

    let mut acc = 0;
    let mut x0 = lines[0].0;

    #[cfg(debug_assertions)]
    println!("\ny_map {y_map:?}");

    for (x, ty, y1, y2) in lines {

        if x != x0 {
            let h = tree.sum();

            acc += ((x - x0) as u64 * h as u64) % M;

            #[cfg(debug_assertions)]
            println!("{x0}-{x}, h: {h}, acc: {acc}");

            x0 = x;
        }

        #[cfg(debug_assertions)]
        if !ty {
            println!("set {y1}-{y2}",);
        }
        else {
            println!("unset {y1}-{y2}")
        }

        tree.update(y1, y2 - 1, ty);

    }

    (acc as u64 % M) as i32
}


fn build_y_discrezation(rectangles: &Vec<Vec<i32>>) -> (Vec<i32>, HashMap<i32, usize>) {
    let mut set = BTreeSet::new();

    for rec in rectangles {
        set.insert(rec[1]);
        set.insert(rec[3]);
    }

    (
        set.iter().cloned().collect(),
        set.into_iter()
            .enumerate()
            .map(|(i, x)| (x, i as usize))
            .collect(),
    )
}

fn build_x_lines(
    rectangles: Vec<Vec<i32>>,
    y_map: &HashMap<i32, usize>,
) -> Vec<(i32, bool, usize, usize)> {
    let mut lines = Vec::with_capacity(rectangles.len() * 2);

    for rec in rectangles {
        let x1 = rec[0];
        let x2 = rec[2];
        let y1 = *y_map.get(&rec[1]).unwrap();
        let y2 = *y_map.get(&rec[3]).unwrap();

        lines.push((x1, true, y1, y2));  // 0  true for enter
        lines.push((x2, false, y1, y2)); // 1  false for exit
    }

    lines.sort_unstable();

    lines
}

struct SegmentTree {
    /// (coverd edges number, range_sum)
    data: Vec<(usize, usize)>,
    y_end: usize,
    y_data: Vec<i32>,
}

/// DFS型
impl SegmentTree {
    fn new(y_data: Vec<i32>, y_end: usize) -> Self {
        SegmentTree {
            // numbers of interval units
            data: vec![(0, 0); (y_end - 1) * 2],
            y_end,
            y_data,
        }
    }

    fn update(&mut self, l: usize, r: usize, mark: bool) {
        self.update_(l, r, 0, self.y_end - 2, 0, mark)
    }

    fn update_(&mut self, l: usize, r: usize, tl: usize, tr: usize, i: usize, mark: bool) {
        if l > r {
            return;
        }

        let mid = (tl + tr) / 2;
        let sub_len = (mid - tl) + 1;

        let i_lf = i + 1;
        let i_rh = i + 2 * sub_len as usize;

        if l == tl && r == tr {
            if mark {
                self.data[i].0 = self.data[i].0 + 1;
            }
            else {
                self.data[i].0 = self.data[i].0 - 1;
            }
        } else {
            self.update_(l, min(mid, r), tl, mid, i_lf, mark);
            self.update_(max(mid + 1, l), r, mid + 1, tr, i_rh, mark);
        }

        if self.data[i].0 > 0 {
            self.data[i].1 = (self.y_data[tr + 1] - self.y_data[tl]) as usize;
        }
        else if tl != tr {
            self.data[i].1 = self.data[i_lf].1 + self.data[i_rh].1;
        }
        else {
            self.data[i].1 = 0;
        }
    }

    fn sum(&self) -> i32 {
        self.data[0].1 as i32
    }
}





fn main() {
    assert_eq!(solve(vec![vec![0,0,1,1], vec![2,2,3,3]]), 2);
    assert_eq!(solve(vec![vec![0,0,2,2],vec![1,1,3,3]]), 7);
    assert_eq!(
        solve(vec![vec![0, 0, 2, 2], vec![1, 0, 2, 3], vec![1, 0, 3, 1]]),
        6
    );
    assert_eq!(solve(vec![vec![0, 0, 1000000000, 1000000000]]), 49);
}
