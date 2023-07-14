//! 61ms (beats 100%), 7.7MB (beats ~100%)


pub fn solve(words: Vec<String>) -> Vec<Vec<i32>> {
    let mut words_and_revs = Vec::with_capacity(words.len() * 2);

    for (i, word) in words.into_iter().enumerate() {
        let forward = word.into_bytes();
        let backward = forward.iter().rev().cloned().collect();

        words_and_revs.push((forward, true, i as i32));
        words_and_revs.push((backward, false, i as i32));
    }

    words_and_revs.sort_unstable();

    let mut ans = vec![];

    for (i, (short, short_is_forward, short_i)) in
        words_and_revs.iter().enumerate()
    {
        for (long, long_is_forward, long_i) in words_and_revs[i + 1..].iter() {
            if short_is_forward == long_is_forward {
                continue;
            }

            if long.starts_with(&short) {
                if long_i != short_i && is_palindrome_or_empty(&long[short.len()..]) {
                    if *long_is_forward {
                        ans.push(vec![*long_i, *short_i]);
                    }
                    else {
                        ans.push(vec![*short_i, *long_i]);
                    }
                }
            }
            else {
                break;
            }
        }
    }

    ans
}


#[inline]
fn is_palindrome_or_empty(s: &[u8]) -> bool {
    s.iter().eq(s.iter().rev())
}



#[cfg(test)]
mod tests {
    use super::*;
    use crate::tests::test_solution;

    #[test]
    fn test_sort_radix() {
        test_solution(solve)
    }
}
