/**
 * Definition of ParentTreeNode:
 *
 * class ParentTreeNode {
 *     public ParentTreeNode parent, left, right;
 * }
 */


public class Solution {
    /*
     * @param root: The root of the tree
     * @param A: node in the tree
     * @param B: node in the tree
     * @return: The lowest common ancestor of A and B
     */
    public ParentTreeNode lowestCommonAncestorII(ParentTreeNode root, ParentTreeNode A, ParentTreeNode B) {
        // write your code here
        // method 2
        // Set<ParentTreeNode> parents = new HashSet<ParentTreeNode>();

        // while (A != null) {
        //     parents.add(A);
        //     A = A.parent;
        // }

        // while (B != null) {
        //     if (parents.contains(B)) return B;

        //     B = B.parent;
        // }

        // return null;

        // method 1
        ParentTreeNode pA = A, pB = B;

        while (pA != pB) {
            pA = (pA == null ? B : pA.parent);
            pB = (pB == null ? A: pB.parent);
        }

        return pA;
    }
}
