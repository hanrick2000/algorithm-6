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
     * @param root: root of the given tree
     * @return: whether it is a mirror of itself
     */
    public boolean isSymmetric(TreeNode root) {
        // Write your code here
        // method 2
        if (root == null) return true;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        q.offer(root);

        while (!q.isEmpty()) {
            TreeNode left = q.poll();
            TreeNode right = q.poll();

            if (left == null && right == null) continue;
            if (left == null || right == null || left.val != right.val) return false;

            q.offer(left.left);
            q.offer(right.right);
            q.offer(left.right);
            q.offer(right.left);
        }

        return true;

        // method 1
        // return root == null || helper(root.left, root.right);
    }

    private boolean helper(TreeNode left, TreeNode right) {
        if (left == null || right == null) return left == right;

        return (left.val == right.val) && helper(left.left, right.right) && helper(left.right, right.left);
    }
}
