# 5 - Two Pointers

## Required (10)

### Naive  228. Middle of Linked List
https://www.lintcode.com/problem/middle-of-linked-list

#### Description
Find the middle node of a linked list.

#### Example
Given 1->2->3, return the node with value 2.

Given 1->2, return the node with value 1.

#### Challenge
If the linked list is in a data stream, can you find the middle without iterating the linked list again?


### Easy  607. Two Sum III - Data structure design
### Easy  539. Move Zeroes

### Easy  521. Remove Duplicate Numbers in Array
https://www.lintcode.com/problem/remove-duplicate-numbers-in-array

#### Description
Given an array of integers, remove the duplicate numbers in it.

You should:

Do it in place in the array.
Move the unique numbers to the front of the array.
Return the total number of the unique numbers.
You don't need to keep the original order of the integers.

#### Example
Given nums = [1,3,1,4,4,2], you should:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

#### Challenge
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.


### Easy  464. Sort Integers II
https://www.lintcode.com/problem/sort-integers-ii

#### Description
Given an integer array, sort it in ascending order. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

#### Example
Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].


### Medium  608. Two Sum II - Input array is sorted
### Medium  143. Sort Colors II
### Medium  57. 3Sum
### Medium  31. Partition Array
### Medium  5. Kth Largest Element

## Optional (10)

#### Easy  604. Window Sum
https://www.lintcode.com/problem/window-sum

#### Description
Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

#### Example
For array [1,2,7,8,5], moving window size k = 3.
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]


### Easy  56. Two Sum
https://www.lintcode.com/problem/two-sum

#### Description
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

You may assume that each input would have exactly one solution

#### Example
numbers=[2, 7, 11, 15], target=9

return [0, 1]

#### Challenge
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time


### Medium  609. Two Sum - Less than or equal to target
### Medium  587. Two Sum - Unique pairs
### Medium  533. Two Sum - Closest to target
### Medium  443. Two Sum - Greater than target
### Medium  461. Kth Smallest Numbers in Unsorted Array
### Medium  382. Triangle Count

### Medium  148. Sort Colors
https://www.lintcode.com/problem/sort-colors

#### Description
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

You are not suppose to use the library's sort function for this problem.
You should do it in-place (sort numbers in the original array).

#### Example
Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].

#### Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?


### Medium  59. 3Sum Closest

## Related (7)

### Medium  894. Pancake Sorting
### Medium  625. Partition Array II

### Medium  610. Two Sum - Difference equals to target
https://www.lintcode.com/problem/two-sum-difference-equals-to-target

#### Description
Given an array of integers, find two numbers that their difference equals to a target value.
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

It's guaranteed there is only one available solution

#### Example
Given nums = [2, 7, 15, 24], target = 5
return [1, 2] (7 - 2 = 5)


### Medium  380. Intersection of Two Linked Lists
https://www.lintcode.com/problem/intersection-of-two-linked-lists

#### Description
Write a program to find the node at which the intersection of two singly linked lists begins.

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.

#### Example
The following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

#### Challenge
Your code should preferably run in O(n) time and use only O(1) memory.


### Medium  102. Linked List Cycle
https://www.lintcode.com/problem/linked-list-cycle

#### Description
Given a linked list, determine if it has a cycle in it.

#### Example
Given -21->10->4->5, tail connects to node index 1, return true

#### Challenge
##### Follow up:
Can you solve it without using extra space?


### Medium  58. 4Sum

### Hard  103. Linked List Cycle II
https://www.lintcode.com/problem/linked-list-cycle-ii

#### Description
Given a linked list, return the node where the cycle begins.

If there is no cycle, return null.

#### Example
Given -21->10->4->5, tail connects to node index 1，return 10
Explanation：
The last node 5 points to the node whose index is 1, which is 10, so the entrance of the ring is 10

#### Challenge
##### Follow up:

Can you solve it without using extra space?
