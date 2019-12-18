/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    private class ResultType {
        public int sum, size;
        ResultType(int sum, int size) {
            this.sum = sum;
            this.size = size;
        }
    }

    private double average;
    private TreeNode node = null;
    /**
     * @param root: the root of binary tree
     * @return: the root of the maximum average of subtree
     */
    public TreeNode findSubtree2(TreeNode root) {
        // write your code here
        helper(root);

        return node;
    }

    private ResultType helper(TreeNode root) {
        if (root == null) return new ResultType(0, 0);

        ResultType left = helper(root.left);
        ResultType right = helper(root.right);

        ResultType result = new ResultType(left.sum + root.val + right.sum, left.size + right.size + 1);

        if (node == null || result.sum * 1.0 / result.size > average) {
            node = root;
            average = result.sum * 1.0 / result.size;
        }

        return result;
    }
}
