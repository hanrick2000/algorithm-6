# 20190104

## 463. Sort Integers
https://www.lintcode.com/problem/sort-integers

### Description
Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.

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


>> ## 93. Balanced Binary Tree

>> ## 95. Validate Binary Search Tree
https://www.lintcode.com/problem/validate-binary-search-tree


----
> ## 17. Subsets (deleted on January 18, 2019)
> ## 18. Subsets II (deleted on January 18, 2019)
> ## 66. Binary Tree Preorder Traversal (deleted on May 30, 2019)
> ## 67. Binary Tree Inorder Traversal (deleted on May 30, 2019)
> ## 68. Binary Tree Postorder Traversal (deleted on May 30, 2019)
> ## 464. Sort Integers II (deleted on May 30, 2019)
> ## 148. Sort Colors (deleted on May 30, 2019)
