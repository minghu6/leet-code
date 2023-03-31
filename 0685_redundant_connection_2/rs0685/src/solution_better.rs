
/// improved edition after read other solutions
pub fn resolve_better(edges: Vec<Vec<i32>>) -> Vec<i32> {
    struct Aux {
        ds: Vec<i32>,
        p: Vec<i32>
    }

    impl Aux {
        fn new(cap: usize) -> Self {
            Self {
                ds: vec![0; cap],
                p: vec![0; cap]
            }
        }

        fn find(&mut self, v: i32) -> i32 {
            let p = self.ds[v as usize];

            if p == 0 {
                v
            }
            else {
                self.ds[v as usize] = self.find(p);

                self.ds[v as usize]
            }
        }

        /// Ignore rank/height compare to save space as we have compressed the path.
        #[inline(always)]
        fn union(&mut self, u: i32, v: i32) -> Result<(), ()> {
            let u_root = self.find(u);
            let v_root = self.find(v);

            if u_root == v_root {
                return Err(());
            }

            self.ds[v_root as usize] = u_root;
            Ok(())
        }

        #[inline(always)]
        fn direct_find(&self, v: i32) -> i32 {
            self.p[v as usize]
        }

        #[inline(always)]
        fn direct_union(&mut self, u: i32, v: i32) {
            self.p[v as usize] = u;
        }
    }

    let mut aux = Aux::new(edges.len() + 1);
    let mut double_head_cand = None;
    let mut cycle_cand = None;

    for e in edges.iter() {
        let u = e[0];
        let v = e[1];

        // found double head
        if aux.direct_find(v) != 0 {
            double_head_cand = Some((u, v));
            continue;
        }

        aux.direct_union(u, v);

        // found cycle (double head case has been excluded)
        if aux.union(u, v).is_err() {
            cycle_cand = Some((u, v));
        }

        if double_head_cand.is_some() && cycle_cand.is_some() { break }
    }

    if double_head_cand.is_none() {
        if let Some((u, v)) = cycle_cand {
            return vec![u, v];
        }
    }
    // 1. the last double head edge cover the cycle edge.
    // 2. no cycle edge.
    else if cycle_cand.is_none() {
        if let Some((u, v)) = double_head_cand {
            return vec![u, v];
        }
    }
    else {
        if let Some((_u, v)) = double_head_cand {
            return vec![aux.direct_find(v), v];
        }
    }

    unreachable!()
}
