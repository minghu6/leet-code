
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

#include <list>
#include <queue>
#include <tuple>
using namespace std;


/// @brief  Modern CPP
TreeNode *addOneRow(TreeNode *root, int val, int depth) {
  if (depth == 1)
    return new TreeNode(val, root, nullptr);

  list<tuple<TreeNode *, int>> ql = {{root, 1}};
  queue<tuple<TreeNode *, int>, list<tuple<TreeNode *, int>>> q(ql);

  while (!q.empty()) {
    TreeNode* node;
    int curd;
    tie(node, curd) = q.front();
    q.pop();

    if (curd == depth - 1) {
      node->left = new TreeNode(val, node->left, nullptr);
      node->right = new TreeNode(val, nullptr, node->right);
    }
    else {
      if (node->left) q.push({node->left, curd+1});
      if (node->right) q.push({node->right, curd+1});
    }

  }

  return root;
}

const int MAX_NODE = 10000;  // 10^4
static TreeNode* qn[MAX_NODE];
static int qd[MAX_NODE];

TreeNode *addOneRow(TreeNode *root, int val, int depth) {
  if (depth == 1)
    return new TreeNode(val, root, nullptr);

  int p = 0;
  qn[p] = root;
  qd[p] = 1;

  while (p >= 0) {
    auto node = qn[p];
    auto curd = qd[p];
    p--;

    if (curd == depth - 1) {
      node->left = new TreeNode(val, node->left, nullptr);
      node->right = new TreeNode(val, nullptr, node->right);
    }
    else {
      if (node->left) {
        qn[++p] = node->left;
        qd[p] = curd+1;
      }
      if (node->right) {
        qn[++p] = node->right;
        qd[p] = curd+1;
      }
    }
  }

  return root;
}
