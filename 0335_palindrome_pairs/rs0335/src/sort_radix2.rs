//! 323ms (beats 100%), 5.8 MB (beats 100%)


pub fn solve(words: Vec<String>) -> Vec<Vec<i32>> {
    let mut words_and_revs = Vec::with_capacity(words.len() * 2);

    for (i, word) in words.iter().enumerate() {
        words_and_revs.push((Slice::new(word.as_bytes(), true), i as i32));
        words_and_revs.push((Slice::new(word.as_bytes(), false), i as i32));
    }

    words_and_revs.sort_unstable();

    let mut ans = vec![];

    for (i, (short, short_i)) in
        words_and_revs.iter().enumerate()
    {
        for (long,  long_i) in words_and_revs[i+1..].iter() {
            if short.dir == long.dir {
                continue;
            }

            if long.starts_with(&short) {
                if long_i != short_i && long.rem_is_palindrome_or_empty(short.len()) {
                    if long.dir {
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


#[derive(PartialEq, Eq)]
struct Slice<'a> {
    raw: &'a [u8],
    dir: bool
}


impl<'a> Slice<'a> {
    fn new(raw: &'a [u8], is_forward: bool) -> Self {
        Self { raw, dir: is_forward }
    }

    #[inline]
    fn len(&self) -> usize {
        self.raw.len()
    }

    fn iter(&'a self) -> Box<dyn Iterator<Item = &u8> + 'a> {
        if self.dir {
            Box::new(self.raw.iter())
        }
        else {
            let mut i = self.raw.len();

            Box::new(std::iter::from_fn(move || {
                if i == 0 {
                    None
                }
                else {
                    i -= 1;
                    Some(&self.raw[i])
                }
            }))
        }
    }

    fn starts_with(&self, other: &Self) -> bool {
        let mut it = self.iter();

        for e in other.iter() {
            if let Some(pe) = it.next() {
                if e != pe {
                    return false;
                }
            }
            else {
                return false
            }
        }

        true
    }

    fn rem_is_palindrome_or_empty(&self, skipped: usize) -> bool {
        if self.dir {
            is_palindrome_or_empty(&self.raw[skipped..])
        }
        else {
            is_palindrome_or_empty(&self.raw[..self.len()-skipped])
        }
    }
}


impl<'a> PartialOrd for Slice<'a> {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        self.iter().partial_cmp(other.iter())
    }
}


impl<'a> Ord for Slice<'a> {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.partial_cmp(&other).unwrap()
    }
}



#[cfg(test)]
mod tests {
    use super::*;
    use crate::tests::test_solution;

    #[test]
    fn test_sort_radix2() {
        test_solution(solve)
    }
}
