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
     * @param root: the root of the given tree
     * @return: the values of the nodes you can see ordered from top to bottom
     */
    public List<Integer> rightSideView(TreeNode root) {
        // write your code here
        List<Integer> result = new ArrayList<>();

        // method 2
        if (root == null) return result;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while (!q.isEmpty()) {
            int last = 0;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                last = node.val;

                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }

            result.add(last);
        }

        // method 1
        // helper(root, result, 0);

        return result;
    }

    private void helper(TreeNode root, List<Integer> result, int level) {
        if (root == null) return;

        if (result.size() == level) result.add(root.val);

        result.set(level, root.val);
        helper(root.left, result, level + 1);
        helper(root.right, result, level + 1);
    }
}
