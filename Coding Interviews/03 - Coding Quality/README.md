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
