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
    // private TreeNode lastNode = null;
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void flatten(TreeNode root) {
        // write your code here
        //if (root == null) return;

        // method 2:
        // flatten(root.right);
        // flatten(root.left);

        // root.right = lastNode;
        // root.left = null;
        // lastNode = root;

        // method 1:
        // if (lastNode != null) {
        //     lastNode.left = null;
        //     lastNode.right = root;
        // }

        // lastNode = root;
        // TreeNode rightNode = root.right;

        // flatten(root.left);
        // flatten(rightNode);

        // method 3:
        helper(root);
    }

    // flattern root and all its children nodes into a list
    // return the list's head and tail.
    private TreeNode[] helper(TreeNode root) {
        if (root == null) return null;

        TreeNode[] leftNode = helper(root.left);
        TreeNode[] rightNode = helper(root.right);

        root.left = null;
        TreeNode tail = root;

        if (leftNode != null) {
            tail.right = leftNode[0];
            tail = leftNode[1];
        }
        if (rightNode != null) {
            tail.right = rightNode[0];
            tail = rightNode[1];
        }

        return new TreeNode[]{root, tail};
    }
}
