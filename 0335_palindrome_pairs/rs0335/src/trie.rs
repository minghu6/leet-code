//! 276ms(beats 100%), 373.2MB(beats 25%) with Vec children
//! 455ms              173.3MB(beats 50%) with HashMap children

use std::collections::HashMap;


pub fn solve(words: Vec<String>) -> Vec<Vec<i32>> {

    let mut trie = PostfixTrie::new();

    for (i, word) in words.iter().enumerate() {
        trie.add_word(i, word.as_bytes());
    }

    let mut ans = vec![];

    for (i, word) in words.iter().enumerate() {
        ans.extend(trie.search_palindrome(i, word.as_bytes()));
    }

    ans
}


struct PostfixTrie {
    nodes: Vec<PostfixTrieNode>,
}


struct PostfixTrieNode {
    is_word: Option<usize>,
    rest_palindromes: Vec<usize>,
    children: HashMap<usize, usize>,
}


impl PostfixTrieNode {
    fn new() -> Self {
        Self {
            is_word: None,
            rest_palindromes: vec![],
            children: HashMap::new(),
        }
    }
}


impl PostfixTrie {
    fn new() -> Self {
        Self {
            nodes: vec![PostfixTrieNode::new()],
        }
    }

    fn push_child(&mut self, p: usize, i: usize) -> usize {
        let node_i = self.nodes.len();

        self.nodes.push(PostfixTrieNode::new());
        self.nodes[p].children.insert(i, node_i);

        node_i
    }

    fn add_word(&mut self, word_i: usize, word: &[u8]) {
        let mut root = 0;

        for i in (1..=word.len()).rev() {
            if is_palindrome(&word[0..i]) {
                self.nodes[root].rest_palindromes.push(word_i);
            }

            let idx = rank(word[i-1]);

            if let Some(&child) = self.nodes[root].children.get(&idx) {
                root = child;
            }
            else {
                root = self.push_child(root, idx);
            }
        }

        self.nodes[root].is_word = Some(word_i);
    }

    fn search_palindrome(&self, word_i: usize, word: &[u8]) -> Vec<Vec<i32>> {
        let mut pairs = vec![];

        let mut root = 0;
        let mut matched = true;

        for i in 0..word.len() {
            if let Some(j) = self.nodes[root].is_word {
                if is_palindrome(&word[i..]) {
                    pairs.push(vec![word_i as _, j as _]);
                }
            }

            let idx = rank(word[i]);

            if let Some(&child) = self.nodes[root].children.get(&idx) {
                root = child;
            }
            else {
                matched = false;
                break;
            }
        }

        if matched {
            if let Some(j) = self.nodes[root].is_word {
                if j != word_i {
                    pairs.push(vec![word_i as _, j as _]);
                }
            }

            pairs.extend(self.nodes[root]
                .rest_palindromes
                .iter()
                .cloned()
                .map(|j| vec![word_i as _, j as _])
            );
        }

        pairs
    }

}


#[inline]
fn rank(c: u8) -> usize {
    (c - 'a' as u8) as _
}


#[inline]
fn is_palindrome(s: &[u8]) -> bool {
    !s.is_empty() && s.iter().eq(s.iter().rev())
}


#[cfg(test)]
mod tests {
    use super::*;
    use crate::tests::test_solution;

    #[test]
    fn test_trie() {
        test_solution(solve)
    }
}
