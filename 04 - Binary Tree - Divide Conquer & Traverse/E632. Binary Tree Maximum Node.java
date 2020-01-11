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
    /*
     * @param root: the root of tree
     * @return: the max node
     */
    public TreeNode maxNode(TreeNode root) {
        // write your code here
        if (root == null) return root;

        TreeNode left = maxNode(root.left);
        TreeNode right = maxNode(root.right);

        return max(max(left, right), root);
    }

    private TreeNode max(TreeNode left, TreeNode right) {
        if (left == null) return right;
        if (right == null) return left;

        return left.val >= right.val ? left : right;
    }
}
