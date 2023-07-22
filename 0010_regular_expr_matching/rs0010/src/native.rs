//! 1 <= s.length <= 20
//! 1 <= p.length <= 20
//!
//! native: 273 ms (beats 10.49%), 2.1 MB(beats 58.4% ~100%)
//! native + fail table: - ms (beats 100%, quicker than 0 ms?) 2.2 MB(beats 24.48% ~100%)
//!


const MAX_S_LEN: usize = 20;
const MAX_LV: usize = MAX_S_LEN / 2;

static mut FAILED: [bool; MAX_LV * MAX_S_LEN] = [false; MAX_LV * MAX_S_LEN];


pub fn solve(s: String, p: String) -> bool {
    let p_bytes = p.as_bytes();
    let s_bytes = s.as_bytes();

    let random_pats: Vec<usize> =
        p.match_indices('*').map(|(i, _)| i - 1).collect();

    /* ZERO '*' */

    if random_pats.is_empty() {
        return match_pat(s_bytes, p_bytes);
    }

    // head & tail quick fail

    let head = random_pats[0]; // s_bytes head i inclusive
    let tail_slice = &p_bytes[random_pats.last().unwrap().clone() + 2..];

    if p_bytes.len() - 2 * random_pats.len() > s_bytes.len() {
        return false;
    }

    let tail = s_bytes.len() - tail_slice.len(); // s_bytes tail i exclusive

    if !match_pat(&s_bytes[..head], &p_bytes[..head]) {
        return false;
    }

    if !match_pat(&s_bytes[tail..], tail_slice) {
        return false;
    }

    /* ONE '*' */

    if random_pats.len() == 1 {
        let c = p_bytes[random_pats[0]];

        return if c == '.' as u8 {
            true
        }
        else {
            s_bytes[head..tail].into_iter().all(|&x| x == c)
        };
    }


    /* >= TWO '*' */

    // fixed pats excluded head and tail
    // (len(fixed_pats) >= 1 for case number(p_bytes contains '*') >= 2)

    let fixed_pats: Vec<&[u8]> = random_pats
        .iter()
        .skip(1)
        .scan(random_pats[0] + 2, |last_i, &i| {
            let slice = &p_bytes[*last_i..i];
            *last_i = i + 2;
            Some(slice)
        })
        .collect();

    let fixed_pats_tot: usize = fixed_pats.iter().map(|s| s.len()).sum();

    if fixed_pats_tot > tail - head {
        return false;
    }

    // match start/end
    // end <= start

    let mut start = head;
    let mut end: usize = tail - fixed_pats_tot;

    let mut fixed_pats_pos = vec![];

    for pat in fixed_pats.iter() {
        let pos: Vec<usize> = (start..=end)
            .filter(|&j| match_pat(&s_bytes[j..j + pat.len()], pat))
            .collect();

        if pos.is_empty() {
            return false;
        }

        fixed_pats_pos.push(pos);

        start += pat.len();
        end += pat.len();
    }


    let mut search_stack = vec![vec![head]];
    let mut lv = 0;
    // i, scale
    let mut bak_range = vec![(0, 0)];

    unsafe { FAILED.fill(false) };

    loop {
        // check fail condition
        while search_stack[lv].is_empty() {
            search_stack.pop();

            if search_stack.is_empty() {
                return false;
            }

            lv -= 1;

            let (i, scale) = bak_range.pop().unwrap();

            let base = lv*MAX_S_LEN + i;
            unsafe { (&mut FAILED[base..=base+scale]).fill(true) }
        }

        let i = search_stack[lv].pop().unwrap();

        if unsafe { FAILED[lv*MAX_S_LEN+i] } {
            continue;
        }

        let c = p_bytes[random_pats[lv]];

        let mut scale = 0;

        if c != '.' as u8 {
            for &s_c in &s_bytes[i..] {
                if s_c != c {
                    break;
                }

                scale += 1;
            }
        }
        else {
            scale = s_bytes.len() - 1; // big enough
        }

        // check succeed condition
        if lv == fixed_pats_pos.len() {
            if i <= tail && i + scale >= tail {
                return true;
            }
        }
        else {
            let pos: Vec<usize> = fixed_pats_pos[lv]
                .iter()
                .filter(|&&j| j >= i && j <= i + scale)
                .map(|&j| j + fixed_pats[lv].len())
                .collect();

            if !pos.is_empty() {
                search_stack.push(pos);
                bak_range.push((i, scale));
                lv += 1;
            }
        }
    }
}


#[inline]
fn match_pat(s: &[u8], pat: &[u8]) -> bool {
    s.len() == pat.len()
        && s.iter()
            .zip(pat.iter())
            .all(|(&c1, &c2)| c2 == '.' as u8 || c2 == c1)
}




#[cfg(test)]
mod tests {
    use super::*;
    use crate::{s, test};


    #[test]
    fn test_naive() {
        test!(solve, "aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*", false);

        test!(solve, "bbcacbabbcbaaccabc", "b*a*a*.c*bb*b*.*.*", true);
        test!(solve, "ac", ".*b*ac*", true);
        test!(solve, "bcbaccbbbccabaac", "c*.*a*b*ac*a*a*", true);
        test!(solve, "aaba", "ab*a*c*a", false);
        test!(solve, "bbcbbcbcbbcaabcacb", "a*.*ac*a*a*.a..*.*", false);
        assert_eq!(solve(s!("mississippi"), s!("mis*is*ip*.")), true);
        assert_eq!(solve(s!("aaa"), s!("ab*ac*a")), true);
        assert_eq!(solve(s!("aab"), s!("c*a*b")), true);
        assert_eq!(solve(s!("a"), s!(".*..")), false);
        assert_eq!(solve(s!("a"), s!("ab*a")), false);

        assert_eq!(solve(s!("aa"), s!("a")), false);
        assert_eq!(solve(s!("aa"), s!("a*")), true);
        assert_eq!(solve(s!("ab"), s!(".*")), true);
    }
}
