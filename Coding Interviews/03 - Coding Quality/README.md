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
