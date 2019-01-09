# 20190104

## 463. Sort Integers
https://www.lintcode.com/problem/sort-integers

### Description
Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.

### Example
Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].


## 464. Sort Integers II
https://www.lintcode.com/problem/sort-integers-ii

### Description
Given an integer array, sort it in ascending order. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

### Example
Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].


## 5. Kth Largest Element
https://www.lintcode.com/problem/kth-largest-element

### Description
Find K-th largest element in an array.

You can swap elements in the array

### Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

### Challenge
O(n) time, O(1) extra memory.


## 148. Sort Colors
https://www.lintcode.com/problem/sort-colors

### Description
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

You are not suppose to use the library's sort function for this problem.
You should do it in-place (sort numbers in the original array).

### Example
Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].

### Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?


## 127. Topological Sorting
https://www.lintcode.com/problem/topological-sorting

### Description
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

You can assume that there is at least one topological order in the graph.

### Clarification
Learn more about representation of graphs

### Example
For graph as follow:

### picture

![Topological Sorting](https://github.com/porrychen/algorithm/blob/master/20190104/127.%20Topological%20Sorting.jpeg?raw=true)

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...

### Challenge
Can you do it in both BFS and DFS?


## 814. Shortest Path in Undirected Graph
https://www.lintcode.com/problem/shortest-path-in-undirected-graph

### Description
Give an undirected graph, in which each edge's length is 1, and give two nodes from the graph. We need to find the length of the shortest path between the given two nodes.

### Example
Given graph = {1,2,4#2,1,4#3,5#4,1,2#5,3}, and nodeA = 3, nodeB = 5.

    1------2  3
     \     |  |
      \    |  |
       \   |  |
        \  |  |
          4   5
return 1.


## 66. Binary Tree Preorder Traversal
https://www.lintcode.com/problem/binary-tree-preorder-traversal

### Description
Given a binary tree, return the preorder traversal of its nodes' values.

### Example
Given:

        1
       / \
      2   3
     / \
    4   5
return [1,2,4,5,3].

### Challenge
Can you do it without recursion?


## 67. Binary Tree Inorder Traversal
https://www.lintcode.com/problem/binary-tree-inorder-traversal

### Description
Given a binary tree, return the inorder traversal of its nodes' values.

### Example
Given binary tree {1,#,2,3},

       1
        \
         2
        /
       3

return [1,3,2].

### Challenge
Can you do it without recursion?


## 68. Binary Tree Postorder Traversal
https://www.lintcode.com/problem/binary-tree-postorder-traversal

### Description
Given a binary tree, return the postorder traversal of its nodes' values.

### Example
Given binary tree {1,#,2,3},

       1
        \
         2
        /
       3

return [3,2,1].

### Challenge
Can you do it without recursion?


## 73. Construct Binary Tree from Preorder and Inorder Traversal
https://www.lintcode.com/problem/construct-binary-tree-from-preorder-and-inorder-traversal

### Description
Given preorder and inorder traversal of a tree, construct the binary tree.

You may assume that duplicates do not exist in the tree.

### Example
Given in-order [1,2,3] and pre-order [2,1,3], return a tree:

      2
     / \
    1   3

### :sparkles: Node

         F
        / \
       D   G
      / \
     B   E
    / \
   A   C

Pre order: [F, D, B, A, E, G]

In order:  [A, B, C, D, E, F, G]

_**Follow the steps below:**_

1st: get the first value in pre order because it is the root value

2nd: find the Position of the root value in in order

3rd: recursive the buildTree function to find root.left and root.right


## 72. Construct Binary Tree from Inorder and Postorder Traversal
https://www.lintcode.com/problem/construct-binary-tree-from-inorder-and-postorder-traversal

### Description
Given inorder and postorder traversal of a tree, construct the binary tree.

You may assume that duplicates do not exist in the tree.

### Example
Given inorder [1,2,3] and postorder [1,3,2], return a tree:

      2
     / \
    1   3


## 97. Maximum Depth of Binary Tree
https://www.lintcode.com/problem/maximum-depth-of-binary-tree

### Description
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Example
Given a binary tree as follow:

      1
     / \
    2   3
       / \
      4   5  
The maximum depth is 3.


## 93. Balanced Binary Tree

### Description
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

### Example
Given binary tree A = {3,9,20,#,#,15,7}, B = {3,#,20,15,7}

    A)  3            B)    3
       / \                  \
      9  20                 20
        /  \                / \
       15   7              15  7
The binary tree A is a height-balanced binary tree, but B is not.


## 95. Validate Binary Search Tree
https://www.lintcode.com/problem/validate-binary-search-tree

### Description
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST

### Example
An example:

      2
     / \
    1   4
       / \
      3   5
The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).


## 17. Subsets
https://www.lintcode.com/problem/subsets

### Description
Given a set of distinct integers, return all possible subsets.

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

### Example
If S = [1,2,3], a solution is:

    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]

### Challenge
Can you do it in both recursively and iteratively?
