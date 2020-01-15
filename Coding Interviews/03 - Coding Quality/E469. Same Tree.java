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
     * @param a: the root of binary tree a.
     * @param b: the root of binary tree b.
     * @return: true if they are identical, or false.
     */
    public boolean isIdentical(TreeNode a, TreeNode b) {
        // write your code here
        if (a == null && b == null) return true;

        // method 2
        if (!check(a, b)) return false;

        Queue<TreeNode> qA = new LinkedList<>();
        qA.offer(a);
        Queue<TreeNode> qB = new LinkedList<>();
        qB.offer(b);

        while (!qA.isEmpty()) {
            a = qA.poll();
            b = qB.poll();
            if (!check(a, b)) return false;

            if (a != null) {
                if (!check(a.left, b.left)) return false;
                if (a.left != null) {
                    qA.offer(a.left);
                    qB.offer(b.left);
                }
                if (!check(a.right, b.right)) return false;
                if (a.right != null) {
                    qA.offer(a.right);
                    qB.offer(b.right);
                }
            }
        }

        return true;

        // method 1
        // if (a != null && b != null) {
        //     return a.val == b.val && isIdentical(a.left, b.left) && isIdentical(a.right, b.right);
        // }

        // return false;
    }

    private boolean check(TreeNode a, TreeNode b) {
        if (a == null && b == null) return true;

        return !(a == null || b == null || a.val != b.val);
    }
}
