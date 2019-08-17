# 02 - Basic Knowledge

## Required(9)

### Naive 366. Fibonacci
https://www.lintcode.com/problem/fibonacci
https://leetcode.com/problems/fibonacci-number/

#### Description

Find the Nth number in Fibonacci sequence.

A Fibonacci sequence is defined as follow:

    * The first two numbers are 0 and 1.
    * The i th number is the sum of i-1 th number and i-2 th number.
The first ten numbers in Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

    The Nth fibonacci number won't exceed the max value of signed 32-bit integer in the test cases.

#### Example
##### Example 1:
  	Input:  1
  	Output: 0

  	Explanation:
  	return the first number in  Fibonacci sequence .

##### Example 2:
  	Input:  2
  	Output: 1

  	Explanation:
  	return the second number in  Fibonacci sequence .


### Easy  204. Singleton
https://www.lintcode.com/problem/singleton/

#### Description

Singleton is a most widely used design pattern. If a class has and only has one instance at every moment, we call this design as singleton. For example, for class Mouse (not a animal mouse), we should design it in singleton.

You job is to implement a getInstance method for given class, return the same instance of this class every time you call this method.

#### Example

    In Java:

    	A a = A.getInstance();
    	A b = A.getInstance();

    a should equal to b.

#### Challenge
If we call getInstance concurrently, can you make sure your code could run correctly?


### Easy212. Space Replacement
### Easy365. Count 1 in Binary

### Easy 35. Reverse Linked List
https://www.lintcode.com/problem/reverse-linked-list/
https://leetcode.com/problems/reverse-linked-list/

#### Description

Reverse a linked list.

#### Example
##### Example 1:

    Input: 1->2->3->null
    Output: 3->2->1->null
##### Example 2:

    Input: 1->2->3->4->null
    Output: 4->3->2->1->null

#### Challenge
Reverse it in-place and in one-pass


### Medium159. Find Minimum in Rotated Sorted Array
### Medium73. Construct Binary Tree from Preorder and Inorder Traversal
### Medium40. Implement Queue by Two Stacks
### Medium38. Search a 2D Matrix II

## Optional(6)

### Easy111. Climbing Stairs
### Easy28. Search a 2D Matrix
### Medium208. Assignment Operator Overloading (C++ Only)
### Medium160. Find Minimum in Rotated Sorted Array II
### Medium72. Construct Binary Tree from Inorder and Postorder Traversal
### Medium36. Reverse Linked List II
