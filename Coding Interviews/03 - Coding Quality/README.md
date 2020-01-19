# 03 - Coding Quality

## Required(8)

### Easy 373. Partition Array by Odd and Even
https://www.lintcode.com/problem/partition-array-by-odd-and-even/

#### Description

Partition an integers array into odd number first and even number second.
    The answer is not unique. All you have to do is give a valid answer.

#### Example
##### Example 1:

    Input: [1,2,3,4]
    Output: [1,3,2,4]
##### Example 2:

    Input: [1,4,2,3,5,6]
    Output: [1,3,5,4,2,6]

#### Challenge
Do it in-place.


### Easy 372. Delete Node in a Linked List
https://www.lintcode.com/problem/delete-node-in-a-linked-list/
https://leetcode.com/problems/delete-node-in-a-linked-list/

#### Description

Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

#### Example
##### Example 1:

    Input:
    1->2->3->4->null
    3
    Output:
    1->2->4->null
##### Example 2:

    Input:
    1->3->5->null
    3
    Output:
    1->5->null


### Easy 174. Remove Nth Node From End of List
https://www.lintcode.com/problem/remove-nth-node-from-end-of-list/
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

#### Description

Given a linked list, remove the nth node from the end of list and return its head.

    The minimum number of nodes in list is n.

#### Example
##### Example 1:
  	Input: list = 1->2->3->4->5->null， n = 2
  	Output: 1->2->3->5->null

##### Example 2:
  	Input:  list = 5->4->3->2->1->null, n = 2
  	Output: 5->4->3->1->null

#### Challenge
Can you do it without getting the length of the linked list?


### Easy165. Merge Two Sorted Lists
### Easy35. Reverse Linked List

### Medium 245. Subtree
https://www.lintcode.com/problem/subtree/

#### Description

You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes. Create an algorithm to decide if T2 is a subtree of T1.

    A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.

#### Example
##### Example 1:

    Input：{1,2,3,#,#,4},{3,4}
    Output：true
    Explanation：
    T2 is a subtree of T1 in the following case:
               1                3
              / \              /
        T1 = 2   3      T2 =  4
                /
               4
##### Example 2:

    Input：{1,2,3,#,#,4},{3,#,4}
    Output：false
    Explanation：
    T2 isn't a subtree of T1 in the following case:

               1               3
              / \               \
        T1 = 2   3       T2 =    4
                /
               4


### Medium371. Print Numbers by Recursion
### Medium140. Fast Power


### Medium 223. Palindrome Linked List

#### Description

Implement a function to check if a linked list is a palindrome.

#### Example
##### Example 1:

    Input: 1->2->1
    output: true
##### Example 2:

    Input: 2->2->1
    output: false
#### Challenge
Could you do it in O(n) time and O(1) space?


### Easy 1003. Binary Tree Pruning
https://leetcode.com/problems/binary-tree-pruning/

#### Description

Given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return this tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

    The binary tree will have at most 100 nodes.
    The value of each node will only be 0 or 1.

#### Example
##### Example 1:

    Input: {1,#,0,0,1}
    Output: {1,#,0,#,1}
    Explanation:
      Only the red nodes satisfy the property "every subtree not containing a 1".
      The diagram on the right represents the answer.

##### Example 2:

    Input: {1,0,1,0,0,0,1}
    Output: {1,#,1,#,1}

##### Example 3:

    Input: {1,1,0,1,1,0,1,0}
    Output: {1,1,0,1,1,#,1}

### Easy 469. Same Tree
https://leetcode.com/problems/same-tree/

#### Description

Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.

#### Example
##### Example 1:

    Input:{1,2,2,4},{1,2,2,4}
    Output:true
    Explanation:
            1                   1
           / \                 / \
          2   2   and         2   2
         /                   /
        4                   4

    are identical.
##### Example 2:

    Input:{1,2,3,4},{1,2,3,#,4}
    Output:false
    Explanation:

            1                  1
           / \                / \
          2   3   and        2   3
         /                        \
        4                          4

    are not identical.
### Easy 376. Binary Tree Path Sum
https://leetcode.com/problems/path-sum

#### Description

Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.

#### Example
##### Example 1:

    Input:
    {1,2,4,2,3}
    5
    Output: [[1, 2, 2],[1, 4]]
    Explanation:
    The tree is look like this:
    	     1
    	    / \
    	   2   4
    	  / \
    	 2   3
    For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5
##### Example 2:

    Input:
    {1,2,4,2,3}
    3
    Output: []
    Explanation:
    The tree is look like this:
    	     1
    	    / \
    	   2   4
    	  / \
    	 2   3
    Notice we need to find all paths from root node to leaf nodes.
    1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5
    There is no one satisfying it.

### Easy 1115. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/

#### Description

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

    The range of node's value is in the range of 32-bit signed integer.

#### Example
##### Example 1:

    Input:
        3
       / \
      9  20
        /  \
       15   7
    Output: [3, 14.5, 11]
    Explanation:
    The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

### Easy 1106. Maximum Binary Tree
https://leetcode.com/problems/maximum-binary-tree

#### Description

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and return the root node of this tree.

    The size of the given array will be in the range of [1,1000].

#### Example
##### Example 1:

    Input: {3,2,1,6,0,5}
    Output: Return the tree root node representing the following tree:
         6
       /   \
      3     5
       \   /
        2 0   
         \
          1
##### Example 2:

    Input: {1,2,3,4}
    Output: Return the tree root node representing the following tree:
            4
           /
          3
         /
        2
       /
      1

### Easy 1094. Second Minimum Node In a Binary Tree
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree

#### Description

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is not bigger than its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

#### Example
##### Example 1:

    Input:
        2
       / \
      2   5
         / \
        5   7

    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.
##### Example 2:

    Input:
        2
       / \
      2   2

    Output: -1
    Explanation: The smallest value is 2, but there isn't any second smallest value.

### Easy 1033. Minimum Difference Between BST Nodes
https://leetcode.com/problems/minimum-distance-between-bst-nodes/

#### Description

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

    1.The size of the BST will be between 2 and 100.
    2.The BST is always valid, each node's value is an integer, and each node's value is different.

#### Example
##### Example 1:

    Input: root = {4,2,6,1,3,#,#}
    Output: 1
    Explanation:
    Note that root is a TreeNode object, not an array.

    The given tree {4,2,6,1,3,#,#} is represented by the following diagram:

              4
            /   \
          2      6
         / \    
        1   3  

    while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
##### Example 2:

    Input: root = {5,1,8}
    Output: 3
    Explanation:
    Note that root is a TreeNode object, not an array.

    The given tree {5,1,8} is represented by the following diagram:

         5
       /   \
     1      8

    while the minimum difference in this tree is 3, it occurs between node 5 and node 8.

### Easy 1165. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

#### Description

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

#### Example
##### Example 1:

    Given tree s:

         3
        / \
       4   5
      / \
     1   2
    Given tree t:
       4
      / \
     1   2
    Return true, because t has the same structure and node values with a subtree of s.
##### Example 2:

    Given tree s:

         3
        / \
       4   5
      / \
     1   2
        /
       0
    Given tree t:
       4
      / \
     1   2
    Return false.

### Easy 1172. Binary Tree Tilt
https://leetcode.com/problems/binary-tree-tilt/

#### Description
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

    1.The sum of node values in any subtree won't exceed the range of 32-bit integer.
    2.All the tilt values won't exceed the range of 32-bit integer.

#### Example
##### Example 1:

    Input:
    {1,2,3}
    Output: 1

    Explanation:
             1
           /   \
          2     3
    Tilt of node 2 : 0
    Tilt of node 3 : 0
    Tilt of node 1 : |2-3| = 1
    Tilt of binary tree : 0 + 0 + 1 = 1
##### Example 2:

    Input：
    {1,1,#,2,3}
    Output：
    7

    Explanation：
            1
          /
        1
       /  \
    2     3

### Easy 1254. Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves/

#### Description

Find the sum of all left leaves in a given binary tree.

#### Example
##### Example 1

    Input：
    {3,9,20,#,#,15,7}
    Output：24

    Explanation：There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
        3
       / \
      9  20
        /  \
       15   7
##### Example 2:

    Input:
    {1,#,2,#,3}
    Output:
    0

    Explanatinon:
    1
      \
        2
          \
           3

### Easy 1360. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/

#### Description

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

#### Example
##### Example1

    Input: {1,2,2,3,4,4,3}
    Output: true
    Explanation:
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    This binary tree {1,2,2,3,4,4,3} is symmetric
##### Example2

    Input: {1,2,2,#,3,#,3}
    Output: false
    Explanation:
        1
       / \
      2   2
       \   \
       3    3
    This is not a symmetric tree
####Challenge
Could you solve it both recursively and iteratively?

### Easy 1495. Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees

#### Description

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

    Both of the given trees will have between 1 and 100 nodes.

#### Example
##### Example 1:

    Input: {1,#,2,3}, {1,2,#,3}
    Output:
    Explaination:
    the first tree:
      1
        \                
         2                
        /                 
       3   
    the second tree:
        1
       /
      2
     /
    3
    The leaf value sequence is: [3], so the same
##### Example 2:

    Input: {1,#,2,3}, {1,2,#,3}
    Output:
    Explaination:
    the first tree:
      1
        \                
         2                
        /                 
       3   
    the second tree:
       1
      / \                
     2   3    
    The first leaf value sequence is: [3], the second tree is: [2, 3], so it is not the same.
