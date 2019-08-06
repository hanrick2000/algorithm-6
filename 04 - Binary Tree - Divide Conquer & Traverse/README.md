# 4 - Binary Tree - Divide Conquer & Traverse

## Required (10)

### Easy  900. Closest Binary Search Tree Value
https://www.lintcode.com/problem/closest-binary-search-tree-value/

#### Description

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

* Given target value is a floating point.
* You are guaranteed to have only one unique value in the BST that is closest to the target.

#### Example
##### Example1

    Input: root = {5,4,9,2,#,8,10} and target = 6.124780
    Output: 5
    Explanation：
    Binary tree {5,4,9,2,#,8,10},  denote the following structure:
            5
           / \
         4    9
        /    / \
       2    8  10
##### Example2

    Input: root = {3,2,4,1} and target = 4.142857
    Output: 4
    Explanation：
    Binary tree {3,2,4,1},  denote the following structure:
         3
        / \
      2    4
     /
    1


### Easy  596. Minimum Subtree
https://www.lintcode.com/problem/minimum-subtree/

#### Description

Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

    LintCode will print the subtree which root is your return node.
    It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

#### Example
##### Example 1:

    Input:
    {1,-5,2,1,2,-4,-5}
    Output:1
    Explanation:
    The tree is look like this:
         1
       /   \
     -5     2
     / \   /  \
    1   2 -4  -5
    The sum of whole tree is minimum, so return the root.
##### Example 2:

    Input:
    {1}
    Output:1
    Explanation:
    The tree is look like this:
       1
    There is one and only one subtree in the tree. So we return 1.


### Easy  480. Binary Tree Paths
https://www.lintcode.com/problem/binary-tree-paths/
https://leetcode.com/problems/binary-tree-paths/

#### Description

Given a binary tree, return all root-to-leaf paths.

#### Example
##### Example 1:

    Input：{1,2,3,#,5}
    Output：["1->2->5","1->3"]
    Explanation：
       1
     /   \
    2     3
     \
      5
##### Example 2:

    Input：{1,2}
    Output：["1->2"]
    Explanation：
       1
     /   
    2    


### Easy  453. Flatten Binary Tree to Linked List
https://www.lintcode.com/problem/flatten-binary-tree-to-linked-list/
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

#### Description

Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

    Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

#### Example
##### Example 1:

    Input:{1,2,5,3,4,#,6}
    Output：{1,#,2,#,3,#,4,#,5,#,6}
    Explanation：
         1
        / \
       2   5
      / \   \
     3   4   6

    1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
##### Example 2:

    Input:{1}
    Output:{1}
    Explanation：
             1
             1
#### Challenge
Do it in-place without any extra memory.


### Easy  93. Balanced Binary Tree
https://www.lintcode.com/problem/balanced-binary-tree/

#### Description
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

#### Example
##### Example  1:
  	Input: tree = {1,2,3}
  	Output: true

  	Explanation:
  	This is a balanced binary tree.
  		  1  
  		 / \                
  		2  3

##### Example  2:
    Given binary tree A = {3,9,20,#,#,15,7}, B = {3,#,20,15,7}

        A)  3            B)    3
           / \                  \
          9  20                 20
            /  \                / \
           15   7              15  7
    The binary tree A is a height-balanced binary tree, but B is not.

##### Example  3:
    	Input: tree = {1,#,2,3,4}
    	Output: false

    	Explanation:
    	This is not a balanced tree.
    	The height of node 1's right sub-tree is 2 but left sub-tree is 0.
    		  1  
    		   \                
    		   2                
    		  /  \                
    		 3   4


### Medium  902. Kth Smallest Element in a BST
https://www.lintcode.com/problem/kth-smallest-element-in-a-bst/

#### Description

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

    You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

#### Example
##### Example 1:

    Input：{1,#,2},2
    Output：2
    Explanation：
    	1
    	 \
    	  2
    The second smallest element is 2.
##### Example 2:

    Input：{2,1,3},1
    Output：1
    Explanation：
      2
     / \
    1   3
    The first smallest element is 1.
#### Challenge
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?


### Medium  578. Lowest Common Ancestor III
https://www.lintcode.com/problem/lowest-common-ancestor-iii/

#### Description

Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Return null if LCA does not exist.

    node A or node B may not exist in tree.

#### Example
##### Example1

    Input:
    {4, 3, 7, #, #, 5, 6}
    3 5
    5 6
    6 7
    5 8
    Output:
    4
    7
    7
    null
    Explanation:
      4
     / \
    3   7
       / \
      5   6

    LCA(3, 5) = 4
    LCA(5, 6) = 7
    LCA(6, 7) = 7
    LCA(5, 8) = null

##### Example2

    Input:
    {1}
    1 1
    Output:
    1
    Explanation:
    The tree is just a node, whose value is 1.


### Medium  95. Validate Binary Search Tree
https://www.lintcode.com/problem/validate-binary-search-tree/

#### Description
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node's key.
* The right subtree of a node contains only nodes with keys greater than the node's key.
* Both the left and right subtrees must also be binary search trees.
* A single node tree is a BST

#### Example
##### Example 1:

    Input:  {-1}
    Output：true
    Explanation：
    For the following binary tree（only one node）:
    	      -1
    This is a binary search tree.

##### Example 2:

          2
         / \
        1   4
           / \
          3   5
    The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).
    Output: true


### Hard  901. Closest Binary Search Tree Value II
https://www.lintcode.com/problem/closest-binary-search-tree-value-ii/

### Hard  86. Binary Search Tree Iterator
https://www.lintcode.com/problem/binary-search-tree-iterator/

## Optional (12)

### Easy  597. Subtree with Maximum Average
https://www.lintcode.com/problem/subtree-with-maximum-average/

### Easy  474. Lowest Common Ancestor II
https://www.lintcode.com/problem/lowest-common-ancestor-ii/

#### Description

Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

The node has an extra attribute parent which point to the father of itself. The root's parent is null.

#### Example
##### Example 1:

    Input：{4,3,7,#,#,5,6},3,5
    Output：4
    Explanation：
         4
         / \
        3   7
           / \
          5   6
    LCA(3, 5) = 4
##### Example 2:

    Input：{4,3,7,#,#,5,6},5,6
    Output：7
    Explanation：
          4
         / \
        3   7
           / \
          5   6
    LCA(5, 6) = 7


### Easy  246. Binary Tree Path Sum II
https://www.lintcode.com/problem/binary-tree-path-sum-ii/

#### Description

Your are given a binary tree in which each node contains a value. Design an algorithm to get all paths which sum to a given value. The path does not need to start or end at the root or a leaf, but it must go in a straight line down.

#### Example
##### Example 1:

    Input:
    {1,2,3,4,#,2}
    6
    Output:
    [[2, 4],[1, 3, 2]]
    Explanation:
    The binary tree is like this:
        1
       / \
      2   3
     /   /
    4   2
    for target 6, it is obvious 2 + 4 = 6 and 1 + 3 + 2 = 6.
##### Example 2:

    Input:
    {1,2,3,4}
    10
    Output:
    []
    Explanation:
    The binary tree is like this:
        1
       / \
      2   3
     /   
    4   
    for target 10, there is no way to reach it.


### Easy  155. Minimum Depth of Binary Tree
https://www.lintcode.com/problem/minimum-depth-of-binary-tree/
https://leetcode.com/problems/minimum-depth-of-binary-tree/

#### Description

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

#### Example
##### Example 1:

    Input: {}
    Output: 0
##### Example 2:

    Input:  {1,#,2,3}
    Output: 3
    Explanation:
    	1
    	 \
    	  2
    	 /
    	3    
    it will be serialized {1,#,2,3}
##### Example 3:

    Input:  {1,2,3,#,#,4,5}
    Output: 2
    Explanation:
          1
         / \
        2   3
           / \
          4   5  
    it will be serialized {1,2,3,#,#,4,5}


### Easy  97. Maximum Depth of Binary Tree
https://www.lintcode.com/problem/maximum-depth-of-binary-tree/

#### Description
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#### Example
##### Example 1:

    Input: tree = {}
    Output: 0
    Explanation: The height of empty tree is 0.
##### Example 2:
    Given a binary tree {1,2,3,#,#,4,5} as follow:

          1
         / \
        2   3
           / \
          4   5  
    The maximum depth is 3.


### Easy  68. Binary Tree Postorder Traversal
https://www.lintcode.com/problem/binary-tree-postorder-traversal

#### Description
Given a binary tree, return the postorder traversal of its nodes' values.

#### Example
Given binary tree {1,#,2,3},

       1
        \
         2
        /
       3

return [3,2,1].

#### Challenge
Can you do it without recursion?


### Easy  67. Binary Tree Inorder Traversal
https://www.lintcode.com/problem/binary-tree-inorder-traversal

#### Description
Given a binary tree, return the inorder traversal of its nodes' values.

#### Example
Given binary tree {1,#,2,3},

       1
        \
         2
        /
       3

return [1,3,2].

#### Challenge
Can you do it without recursion?


### Easy  66. Binary Tree Preorder Traversal
https://www.lintcode.com/problem/binary-tree-preorder-traversal

#### Description
Given a binary tree, return the preorder traversal of its nodes' values.

#### Example
Given:

        1
       / \
      2   3
     / \
    4   5
return [1,2,4,5,3].

#### Challenge
Can you do it without recursion?


### Medium  915. Inorder Predecessor in BST
https://www.lintcode.com/problem/inorder-predecessor-in-bst/

### Medium  448. Inorder Successor in BST
https://www.lintcode.com/problem/inorder-successor-in-bst/

### Medium  88. Lowest Common Ancestor of a Binary Tree
https://www.lintcode.com/problem/lowest-common-ancestor-of-a-binary-tree/

### Hard  472. Binary Tree Path Sum III
https://www.lintcode.com/problem/binary-tree-path-sum-iii/

## Related (6)

### Easy  595. Binary Tree Longest Consecutive Sequence
https://www.lintcode.com/problem/binary-tree-longest-consecutive-sequence/

#### Description

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

#### Example
##### Example 1:

    Input:
       1
        \
         3
        / \
       2   4
            \
             5
    Output:3
    Explanation:
    Longest consecutive sequence path is 3-4-5, so return 3.
##### Example 2:

    Input:
       2
        \
         3
        /
       2    
      /
     1
    Output:2
    Explanation:
    Longest consecutive sequence path is 2-3,not 3-2-1, so return 2.


### Medium  619. Binary Tree Longest Consecutive Sequence III
https://www.lintcode.com/problem/binary-tree-longest-consecutive-sequence-iii/

### Medium  614. Binary Tree Longest Consecutive Sequence II
https://www.lintcode.com/problem/binary-tree-longest-consecutive-sequence-ii/

### Medium  520. Consistent Hashing II
https://www.lintcode.com/problem/consistent-hashing-ii/

### Medium  475. Binary Tree Maximum Path Sum II
https://www.lintcode.com/problem/binary-tree-maximum-path-sum-ii/

### Medium  94. Binary Tree Maximum Path Sum
https://www.lintcode.com/problem/binary-tree-maximum-path-sum/

## -------------------

### Easy 1126. Merge Two Binary Trees
https://www.lintcode.com/problem/merge-two-binary-trees/
https://leetcode.com/problems/merge-two-binary-trees/

#### Description

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

    The merging process must start from the root nodes of both trees.

#### Example
##### Example1

    Input:
    {1,3,2,5}
    {2,1,3,#,4,#,7}
    Output:
    {3,4,5,5,4,#,7}
    Explanation:
    	Tree 1                     Tree 2                  
              1                         2                             
             / \                       / \                            
            3   2                     1   3                        
           /                           \   \                      
          5                             4   7                  

    Merged tree:
    	     3
    	    / \
    	   4   5
    	  / \   \
    	 5   4   7
##### Example2

    Input:
    {1}
    {1,2}
    Output:
    {2,2}
