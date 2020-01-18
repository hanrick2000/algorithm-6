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
    /**
     * @param root: t
     * @return: the sum of all left leaves
     */
    public int sumOfLeftLeaves(TreeNode root) {
        // Write your code here
        int sum = 0;
        if (root == null) return sum;

        if (root.left != null) {
            TreeNode left = root.left;
            if (left.left == null && left.right == null) {
                sum += left.val;
            } else {
                sum += sumOfLeftLeaves(left);
            }
        }

        if (root.right != null) {
            sum += sumOfLeftLeaves(root.right);
        }

        return sum;
    }
}
