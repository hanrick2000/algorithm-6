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
     * @param root: a root of integer
     * @return: return a list of integer
     */
    public List<Integer> largestValues(TreeNode root) {
        // write your code here
        List<Integer> result = new ArrayList<>();

        // method 2
        if (root == null) return result;

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while (!q.isEmpty()) {
            int max = Integer.MIN_VALUE;
            int size = q.size();

            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                if (max < node.val) max = node.val;

                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }

            result.add(max);
        }

        // method 1
        // helper(root, result, 0);

        return result;
    }

    private void helper(TreeNode root, List<Integer> result, int level) {
        if (root == null) return;

        if (result.size() == level) {
            result.add(Integer.MIN_VALUE);
        }

        if (result.get(level) < root.val) result.set(level, root.val);

        helper(root.left, result, level + 1);
        helper(root.right, result, level + 1);
    }
}
