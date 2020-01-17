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
     * @return: the tilt of the whole tree
     */
    public int findTilt(TreeNode root) {
        // Write your code here
        return countTree(root)[1];
    }

    private int[] countTree(TreeNode root) {
        if (root == null) return new int[] {0, 0};

        int[] left = countTree(root.left);
        int[] right = countTree(root.right);

        return new int[] {root.val + left[0] + right[0], left[1] + right[1] + Math.abs(left[0] - right[0])};
    }
}
