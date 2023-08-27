const MAX_S_LEN: usize = 20;

static mut CUR: [bool; MAX_S_LEN + 1] = [false; MAX_S_LEN + 1];
static mut PRE1: [bool; MAX_S_LEN + 1] = [false; MAX_S_LEN + 1];


/// Running Time Saving
/// patten-text [j][i]
pub fn solve_time_saving(s: String, p: String) -> bool {
    unsafe {
        let p_bytes = p.as_bytes();
        let s_bytes = s.as_bytes();

        CUR[1..=s_bytes.len()].fill(false);
        CUR[0] = true;

        for j in 1..=p_bytes.len() {
            if p_bytes[j - 1] == '*' as u8 {
                // The valid pattern has guaranteed that j >= 2
                if p_bytes[j - 2] == '.' as u8 {
                    for i in 0..=s_bytes.len() {
                        let pre2 = PRE1[i];
                        PRE1[i] = CUR[i];
                        CUR[i] = pre2 || i > 0 && CUR[i - 1];
                    }
                }
                else {
                    for i in 0..=s_bytes.len() {
                        let pre2 = PRE1[i];
                        PRE1[i] = CUR[i];
                        CUR[i] = pre2
                            || i > 0
                                && p_bytes[j - 2] == s_bytes[i - 1]
                                && CUR[i - 1]
                    }
                }
            }
            else if p_bytes[j - 1] == '.' as u8 {
                PRE1[..=s_bytes.len()].copy_from_slice(&CUR[..=s_bytes.len()]);

                CUR[0] = false;

                for i in 1..=s_bytes.len() {
                    CUR[i] = PRE1[i - 1];
                }
            }
            else {
                PRE1[..=s_bytes.len()].copy_from_slice(&CUR[..=s_bytes.len()]);

                CUR[0] = false;

                for i in 1..=s_bytes.len() {
                    CUR[i] = p_bytes[j - 1] == s_bytes[i - 1] && PRE1[i-1];
                }
            }
        }

        CUR[s_bytes.len()]
    }

}


macro_rules! char_match {
    ($p:expr, $s:expr) => {
        ($p == '.' as _ || $p == $s)
    };
}

static mut DP: [bool; MAX_S_LEN + 1] = [false; MAX_S_LEN + 1];


pub fn solve_mem_saving(s: String, p: String) -> bool {
    unsafe {
        let p_bytes = p.as_bytes();
        let s_bytes = s.as_bytes();

        DP[1..=s_bytes.len()].fill(false);
        DP[0] = true;

        for j in 1..=p_bytes.len() {
            if p_bytes[j - 1] == '*' as _ {
                DP[j] = DP[j - 2];
            }
        }

        // ..i

        for i in 1..=s_bytes.len() {
            let mut pre_1 = DP[0];
            DP[0] = false;

            for j in 1..=p_bytes.len() {
                let pre_0 = DP[j];

                if p_bytes[j - 1] == '*' as _ {
                    DP[j] = DP[j - 2]
                        || pre_0
                            && char_match!(p_bytes[j - 2], s_bytes[i - 1]);
                }
                else {
                    DP[j] =
                        pre_1 && char_match!(p_bytes[j - 1], s_bytes[i - 1]);
                }

                pre_1 = pre_0;
            }
        }

        DP[p_bytes.len()]
    }
}



#[cfg(test)]
mod tests {
    use super::*;
    use crate::{s, test};


    #[test]
    fn test_dp_time_saving() {
        test!(solve_time_saving, "ac", ".*b*ac*", true);

        test!(
            solve_time_saving,
            "aaaaaaaaaaaaaaaaaaab",
            "a*a*a*a*a*a*a*a*a*a*",
            false
        );
        test!(
            solve_time_saving,
            "bbcacbabbcbaaccabc",
            "b*a*a*.c*bb*b*.*.*",
            true
        );
        test!(
            solve_time_saving,
            "bcbaccbbbccabaac",
            "c*.*a*b*ac*a*a*",
            true
        );
        test!(solve_time_saving, "aaba", "ab*a*c*a", false);
        test!(
            solve_time_saving,
            "bbcbbcbcbbcaabcacb",
            "a*.*ac*a*a*.a..*.*",
            false
        );
        assert_eq!(
            solve_time_saving(s!("mississippi"), s!("mis*is*ip*.")),
            true
        );
        assert_eq!(solve_time_saving(s!("aaa"), s!("ab*ac*a")), true);
        assert_eq!(solve_time_saving(s!("aab"), s!("c*a*b")), true);
        assert_eq!(solve_time_saving(s!("a"), s!(".*..")), false);
        assert_eq!(solve_time_saving(s!("a"), s!("ab*a")), false);

        assert_eq!(solve_time_saving(s!("aa"), s!("a")), false);
        assert_eq!(solve_time_saving(s!("aa"), s!("a*")), true);
        assert_eq!(solve_time_saving(s!("ab"), s!(".*")), true);
    }

    #[test]
    fn test_dp_mem_saving() {
        test!(solve_mem_saving, "ac", ".*b*ac*", true);

        test!(
            solve_mem_saving,
            "aaaaaaaaaaaaaaaaaaab",
            "a*a*a*a*a*a*a*a*a*a*",
            false
        );
        test!(
            solve_mem_saving,
            "bbcacbabbcbaaccabc",
            "b*a*a*.c*bb*b*.*.*",
            true
        );
        test!(
            solve_mem_saving,
            "bcbaccbbbccabaac",
            "c*.*a*b*ac*a*a*",
            true
        );
        test!(solve_mem_saving, "aaba", "ab*a*c*a", false);
        test!(
            solve_mem_saving,
            "bbcbbcbcbbcaabcacb",
            "a*.*ac*a*a*.a..*.*",
            false
        );
        assert_eq!(
            solve_mem_saving(s!("mississippi"), s!("mis*is*ip*.")),
            true
        );
        assert_eq!(solve_mem_saving(s!("aaa"), s!("ab*ac*a")), true);
        assert_eq!(solve_mem_saving(s!("aab"), s!("c*a*b")), true);
        assert_eq!(solve_mem_saving(s!("a"), s!(".*..")), false);
        assert_eq!(solve_mem_saving(s!("a"), s!("ab*a")), false);

        assert_eq!(solve_mem_saving(s!("aa"), s!("a")), false);
        assert_eq!(solve_mem_saving(s!("aa"), s!("a*")), true);
        assert_eq!(solve_mem_saving(s!("ab"), s!(".*")), true);
    }
}
