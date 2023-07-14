pub mod trie;
pub mod len_radix;
pub mod sort_radix;
pub mod sort_radix2;


#[cfg(test)]
mod tests {
    #[macro_export]
    macro_rules! arr_to_vec_2 {
        ([
            $(
                [$($e:expr),*]
            ),*
        ]) => {
            vec![$(vec![$($e),*]),*]
        };
    }


    #[macro_export]
    macro_rules! arrstr_to_vecstring {
        ([$($e:expr),*]) => {
            vec![$($e.to_string()),*]
        };
    }

    macro_rules! bag {
        ($e:expr) => {
            {
                let mut e_cache = $e;

                e_cache.sort_unstable();

                e_cache
            }
        };
    }


    pub(crate) fn test_solution(solve: fn(words: Vec<String>) -> Vec<Vec<i32>>) {
        assert_eq!(
            bag!(solve(arrstr_to_vecstring!(["abcd", "dcba", "lls", "s", "sssll"]))),
            bag!(arr_to_vec_2!([[0, 1], [1, 0], [3, 2], [2, 4]]))
        );

        assert_eq!(
            bag!(solve(arrstr_to_vecstring!(["abcd", "dcba", "lls", "s", "sssll"]))),
            bag!(arr_to_vec_2!([[0, 1], [1, 0], [3, 2], [2, 4]]))
        );

        assert_eq!(
            bag!(solve(arrstr_to_vecstring!(["bat", "tab", "cat"]))),
            bag!(arr_to_vec_2!([[0, 1], [1, 0]]))
        );

        assert_eq!(
            bag!(solve(arrstr_to_vecstring!(["a", ""]))),
            bag!(arr_to_vec_2!([[0, 1], [1, 0]]))
        );
    }
}

