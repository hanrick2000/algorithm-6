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
     * @param root1: the first tree
     * @param root2: the second tree
     * @return: returns whether the leaf sequence is the same
     */
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        // write your code here.
        List<Integer> l1 = new ArrayList<>();
        List<Integer> l2 = new ArrayList<>();

        helper(root1, l1);
        helper(root2, l2);

        return l1.equals(l2);
    }

    private void helper(TreeNode root, List<Integer> leaves) {
        if (root == null) return;

        if (root.left == null && root.right == null) leaves.add(root.val);

        helper(root.left, leaves);
        helper(root.right, leaves);
    }
}
