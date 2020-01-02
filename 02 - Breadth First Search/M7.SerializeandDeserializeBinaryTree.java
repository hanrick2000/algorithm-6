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
     * This method will be invoked first, you should design your own algorithm
     * to serialize a binary tree which denote by a root node to a string which
     * can be easily deserialized by your own "deserialize" method later.
     */
    public String serialize(TreeNode root) {
        // write your code here
        if (root == null) return "";

        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while (!q.isEmpty()) {
            TreeNode node = q.poll();

            if (node == null) {
                sb.append("#,");
                continue;
            }

            sb.append(node.val + ",");
            q.offer(node.left);
            q.offer(node.right);
        }

        return sb.toString().substring(0, sb.length() - 1);
    }

    /**
     * This method will be invoked second, the argument data is what exactly
     * you serialized at method "serialize", that means the data is not given by
     * system, it's given by your own serialize method. So the format of data is
     * designed by yourself, and deserialize it here as you serialize it in
     * "serialize" method.
     */
    public TreeNode deserialize(String data) {
        // write your code here
        if (data.equals("")) return null;

        String[] str = data.split(",");
        List<TreeNode> orders = new ArrayList<>();
        for (int i = 0; i < str.length; i++) {
            if (str[i].equals("#")) {
                orders.add(null);
            } else {
                orders.add(new TreeNode(Integer.parseInt(str[i])));
            }
        }
        TreeNode root = orders.get(0);
        List<TreeNode> nodes = new ArrayList<>();
        nodes.add(root);
        int slow = 0, fast = 1;
        while (slow < nodes.size()) {
            TreeNode node = nodes.get(slow++);
            node.left = orders.get(fast++);
            node.right = orders.get(fast++);

            if (node.left != null) nodes.add(node.left);
            if (node.right != null) nodes.add(node.right);
        }

        return root;
    }
}
