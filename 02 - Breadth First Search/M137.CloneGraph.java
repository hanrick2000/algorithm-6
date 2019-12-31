/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */


public class Solution {
    /*
     * @param node: A undirected graph node
     * @return: A undirected graph node
     */
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        // write your code here
        if (node == null) return node;

        ArrayList<UndirectedGraphNode> nodes = getNodes(node);

        Map<UndirectedGraphNode, UndirectedGraphNode> mapping = new HashMap<>();
        for (UndirectedGraphNode n: nodes) {
            mapping.put(n, new UndirectedGraphNode(n.label));
        }

        for (UndirectedGraphNode n: nodes) {
            UndirectedGraphNode newNode = mapping.get(n);
            for (UndirectedGraphNode neighbor: n.neighbors) {
                UndirectedGraphNode newNeighbor = mapping.get(neighbor);
                newNode.neighbors.add(newNeighbor);
            }
        }

        return mapping.get(node);
    }

    private ArrayList<UndirectedGraphNode> getNodes(UndirectedGraphNode node) {
        Queue<UndirectedGraphNode> q = new LinkedList<>();
        q.offer(node);

        Set<UndirectedGraphNode> set = new HashSet<>();
        set.add(node);

        while (!q.isEmpty()) {
            UndirectedGraphNode head = q.poll();
            for (UndirectedGraphNode neighbor: head.neighbors) {
                if (!set.contains(neighbor)) {
                    set.add(neighbor);
                    q.offer(neighbor);
                }
            }
        }

        return new ArrayList<UndirectedGraphNode>(set);
    }
}

// leetcode
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {}

    public Node(int _val,List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return node;

        List<Node> nodes = getNodes(node);

        Map<Node, Node> mapping = new HashMap<>();
        for (Node n: nodes) {
            mapping.put(n, new Node(n.val, new ArrayList<>()));
        }

        for (Node n: nodes) {
            Node newNode = mapping.get(n);
            for (Node neighbor: n.neighbors) {
                Node newNeighbor = mapping.get(neighbor);
                newNode.neighbors.add(newNeighbor);
            }
        }

        return mapping.get(node);
    }

    private List<Node> getNodes(Node node) {
        Queue<Node> q = new LinkedList<>();
        q.offer(node);

        Set<Node> set = new HashSet<>();
        set.add(node);

        while (!q.isEmpty()) {
            Node head = q.poll();
            for (Node neighbor: head.neighbors) {
                if (!set.contains(neighbor)) {
                    set.add(neighbor);
                    q.offer(neighbor);
                }
            }
        }

        return new ArrayList<>(set);
    }
}
