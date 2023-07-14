//! 107ms (beats 100%), 6.6MB (beats 100%)


pub fn solve(words: Vec<String>) -> Vec<Vec<i32>> {
    let mut words_map = std::collections::HashMap::new();
    let mut len_maps = std::collections::BTreeSet::new();

    for (i, word) in words.iter().enumerate() {
        words_map.insert(word.as_bytes(), i);
        len_maps.insert(word.len());
    }

    let lens: Vec<usize> = len_maps.into_iter().collect();

    let mut ans = vec![];

    for (i, word) in words.iter().enumerate() {
        let word = word.as_bytes();

        let rev_word = &word.iter().rev().cloned().collect::<Vec<u8>>();
        let n = word.len();

        for &k in &lens[..lens.binary_search(&n).unwrap()] {
            // word is prefix
            // word[0..k] =R= rev_word[0..k]
            if let Some(&j) = words_map.get(&rev_word[n-k..]) {
                if is_palindrome_or_empty(&word[k..]) {
                    ans.push(vec![i as _, j as _]);
                }
            }

            // word is postfix
            // word[n-k..] => rev_word[n-k..]
            if let Some(&j) = words_map.get(&rev_word[..k]) {
                if is_palindrome_or_empty(&word[..n-k]) {
                    ans.push(vec![j as _, i as _]);
                }
            }
        }

        if let Some(&j) = words_map.get(&rev_word[..]) {
            if word > rev_word {
                ans.push(vec![i as _, j as _]);
                ans.push(vec![j as _, i as _]);
            }
        }
    }

    ans
}


/// Quickest method on len(word) <= 300
#[inline]
fn is_palindrome_or_empty(s: &[u8]) -> bool {
    s.iter().eq(s.iter().rev())
}


#[cfg(test)]
mod tests {
    use super::*;
    use crate::tests::test_solution;

    #[test]
    fn test_len_radix() {
        test_solution(solve)
    }
}
