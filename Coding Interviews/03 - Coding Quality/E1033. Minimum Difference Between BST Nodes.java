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
    private Integer result = Integer.MAX_VALUE, previous = null;

    /**
     * @param root: the root
     * @return: the minimum difference between the values of any two different nodes in the tree
     */
    public int minDiffInBST(TreeNode root) {
        // Write your code here
        if (root.left != null) minDiffInBST(root.left);

        if (previous != null) result = Math.min(result, root.val - previous);
        previous = root.val;

        if (root.right != null) minDiffInBST(root.right);

        return result;
    }
}
