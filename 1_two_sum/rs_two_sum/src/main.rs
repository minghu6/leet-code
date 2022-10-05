#![allow(unused)]

/// T: O(nlog(n)):
///
/// Hybird Sort and then binary search
pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {

    let mut nums: Vec<(usize, i32)> = nums.into_iter()
        .enumerate()
        .collect();

    nums.sort_by_key(|x| x.1);

    for (i, v) in nums.iter().enumerate() {
        let pair = target - v.1;
        if let Ok(ind) = nums[i+1..].binary_search_by_key(&pair, |x| x.1) {
            return vec![nums[i].0 as i32, nums[ind + i+1].0 as i32]
        }
    }

    unreachable!()
}

/// T: O(n)
///
/// using HashMap
///
pub fn two_sum2(nums: Vec<i32>, target: i32) -> Vec<i32> {
    use std::collections::HashMap;

    let mut map = HashMap::with_capacity(nums.len() / 2);

    for (i, v) in nums.into_iter().enumerate() {
        if let Some(res) = map.get(&(target - v)) {
            return vec![i as i32, *res];
        }

        map.insert(v, i as i32);

    }

    unreachable!()
}



fn main() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;
    two_sum(nums, target);
}
