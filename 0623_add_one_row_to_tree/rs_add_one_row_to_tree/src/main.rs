use std::{cell::RefCell, rc::Rc};

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

macro_rules! node {
    ($v:expr, $lf:expr, $rh:expr) => {
        Some(Rc::new(RefCell::new(TreeNode {
            val: $v,
            left: $lf,
            right: $rh,
        })))
    };
}

macro_rules! attr {
    ($node:expr, $attr:ident) => {
        {
            let _unr = $node.clone().unwrap();
            let _bor = _unr.as_ref().borrow();
            let _attr = _bor.$attr.clone();
            drop(_bor);
            _attr
        }
    };
}

macro_rules! mattr {
    ($node:expr, $attr:ident) => {
        $node.clone().unwrap().as_ref().borrow_mut().$attr
    };
}

pub fn add_one_row(
    root: Option<Rc<RefCell<TreeNode>>>,
    val: i32,
    depth: i32,
) -> Option<Rc<RefCell<TreeNode>>> {
    if depth == 1 {
        return node! { val, root, None };
    }

    let mut q = vec![(root.clone(), 1)];
    let td = depth - 1;

    while let Some((node, curd)) = q.pop() {
        if curd == td {
            mattr!(node, left) = node! { val, attr!(node, left), None };
            mattr!(node, right) = node! { val, None, attr!(node, right) };
        }
        else {
            if let Some(_node) = attr!(node, left) {
                q.push((Some(_node), curd + 1));
            }
            if let Some(_node) = attr!(node, right) {
                q.push((Some(_node), curd + 1));
            }
        }
    }

    root
}


fn main() {
    println!("Hello, world!");
}
