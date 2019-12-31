/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
 * };
 */

public class Solution {
    /*
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        // write your code here
        List<DirectedGraphNode> result = new ArrayList<>();
        Map<DirectedGraphNode, Integer> map = new HashMap<>();

        for (DirectedGraphNode node: graph) {
            for (DirectedGraphNode neighbor: node.neighbors) {
                map.put(neighbor, map.getOrDefault(neighbor, 0) + 1);
            }
        }

        Queue<DirectedGraphNode> q = new LinkedList<>();
        for (DirectedGraphNode node: graph) {
            if (!map.containsKey(node)) {
                q.offer(node);
                result.add(node);
            }
        }

        while (!q.isEmpty()) {
            DirectedGraphNode node = q.poll();
            for (DirectedGraphNode neighbor: node.neighbors) {
                map.put(neighbor, map.get(neighbor) - 1);

                if (map.get(neighbor) == 0) {
                    q.offer(neighbor);
                    result.add(neighbor);
                }
            }
        }

        return (ArrayList) result;
    }
}
