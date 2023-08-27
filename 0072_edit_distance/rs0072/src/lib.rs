//!

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

    macro_rules! set {
        ($e:expr) => {
            std::collections::BTreeSet::<Vec<i32>>::from_iter($e)
        };
    }

    #[macro_export]
    macro_rules! min {
        ($($val:expr),+) => {
            {
                [$($val),+].into_iter().min().unwrap()
            }
        };
        ($($val:expr),+;$default:expr) => {
            {
                [$($val),+].into_iter().min().unwrap_or($default)
            }
        }
    }

    #[macro_export]
    macro_rules! max {
        ($($val:expr),+) => {
            {
                [$($val),+].into_iter().max().unwrap()
            }
        };
        ($($val:expr),+;$default:expr) => {
            {
                [$($val),+].into_iter().max().unwrap_or($default)
            }
        }
    }
}

