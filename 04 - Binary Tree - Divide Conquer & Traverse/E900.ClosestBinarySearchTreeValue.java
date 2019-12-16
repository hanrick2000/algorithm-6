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
     * @param root: the given BST
     * @param target: the given target
     * @return: the value in the BST that is closest to the target
     */
    public int closestValue(TreeNode root, double target) {
        // write your code here
        TreeNode lowerNode = root, upperNode = root;

        while (root != null) {
            if (root.val < target) {
                lowerNode = root;
                root = root.right;
            } else if (root.val > target) {
                upperNode = root;
                root = root.left;
            } else return root.val;
        }

        if (Math.abs(lowerNode.val - target) < Math.abs(upperNode.val - target)) return lowerNode.val;

        return upperNode.val;
    }
}
