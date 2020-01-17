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
     * @param root: the root
     * @return: the second minimum value in the set made of all the nodes' value in the whole tree
     */
    public int findSecondMinimumValue(TreeNode root) {
        // Write your code here
        if (root == null || (root.left == null && root.right == null)) return -1;

        int left = root.left.val;
        if (left == root.val) left = findSecondMinimumValue(root.left);

        int right = root.right.val;
        if (right == root.val) right = findSecondMinimumValue(root.right);

        if (left == -1) return right;
        if (right == -1) return left;

        return Math.min(left, right);
    }
}
