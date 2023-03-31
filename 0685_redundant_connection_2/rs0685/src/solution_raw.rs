

/// first edition by union find (partly)
pub fn resolve_raw(edges: Vec<Vec<i32>>) -> Vec<i32> {
    use std::collections::HashSet;

    /// Disjoint Set Union
    struct DSU {
        data: Vec<i32>,
        cycles: HashSet<i32>
    }


    impl DSU {
        fn new(cap: usize) -> Self {
            Self {
                data: vec![0; cap],
                cycles: HashSet::new()
            }
        }

        fn find(&mut self, v: i32) -> Result<i32, i32> {
            let p = self.data[v as usize];

            if p == 0 {
                Ok(v)
            }
            else if self.cycles.contains(&p) {
                Err(p)
            }
            else {
                self.find(p)
                    .and_then(|p| {
                        if !self.cycles.is_empty() {
                            self.data[v as usize] = p;
                        }

                        Ok(p)
                    })
            }
        }

        #[inline(always)]
        fn union(&mut self, u: i32, v: i32) {
            self.data[v as usize] = u;
        }

        fn build_cycle(&mut self, mut u: i32, v: i32) {
            while u != v {
                self.cycles.insert(u);
                u = self.data[u as usize];
            }

            self.cycles.insert(u);
        }

    }

    let mut dsu = DSU::new(edges.len() + 1);

    let mut double_head_cand = None;
    let mut cycle_cand = None;

    for e in edges.iter() {
        let u = e[0];
        let v = e[1];

        // found cycle
        if dsu.find(u) == Ok(v) {
            // build cycle
            dsu.build_cycle(u, v);
            cycle_cand = Some((u, v));
        }

        // found double head
        if dsu.data[v as usize] != 0 {
            let u2 = u;
            let u1 = dsu.data[v as usize];

            double_head_cand = Some((v, u2, u1));
        }
        else {
            dsu.union(u, v);
        }
    }

    // dbg!(double_head_cand, cycle_cand);

    let u;
    let v;

    #[allow(unused_must_use)]
    if let Some((v_, u2, u1)) = double_head_cand {
        v = v_;

        if dsu.cycles.contains(&u1) {
            u = u1;
        }
        else {
            u = u2;
        }
    }
    // for now 2023.03.30, leetcode compiler version (1.58) doesn't accept `unwrap assign`
    else if let Some((u_, v_)) = cycle_cand {
        u = u_;
        v = v_;
    }
    else {
        unreachable!()
    }

    vec![u, v]
}
