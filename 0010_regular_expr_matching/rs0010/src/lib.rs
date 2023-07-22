
pub mod native;
pub mod dp;


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

#[macro_export]
macro_rules! s {
    ($e:expr) => {
        $e.to_string()
    };
}



#[macro_export]
macro_rules! test {
    ($solve:ident, $s:literal, $p:literal, $expect:literal) => {{
        use $crate::*;

        fn print_range(len: usize) -> String {
            use std::fmt::Write;

            let mut cache = String::new();

            for i in 0..len {
                write!(&mut cache, "{i:02} ").unwrap();
            }

            cache
        }

        fn print_string(s: &str) -> String {
            use std::fmt::Write;

            let mut cache = String::new();

            for &c in s.as_bytes() {
                let c = c as char;

                write!(&mut cache, "{c:>2} ").unwrap();
            }

            cache
        }

        assert_eq!(
            $solve(s!($s), s!($p)),
            $expect,
            "\n{}\n{}\n\n{}\n\n",
            print_range($s.len()),
            print_string($s),
            $p
        );
    }};
}

