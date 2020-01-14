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
     * @param A: an integer array
     * @return: A tree node
     */
    public TreeNode sortedArrayToBST(int[] A) {
        // write your code here
        if (A == null || A.length == 0) return null;

        return helper(A, 0, A.length - 1);
    }

    private TreeNode helper(int[] A, int l, int r) {
        if (l > r) return null;

        int mid = l + (r - l) / 2;

        TreeNode root = new TreeNode(A[mid]);
        root.left = helper(A, l, mid - 1);
        root.right = helper(A, mid + 1, r);

        return root;
    }
}
