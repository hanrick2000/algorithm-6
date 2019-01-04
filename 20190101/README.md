# 20190101

## 891. Valid Palindrome II
https://www.lintcode.com/problem/valid-palindrome-ii

### Description
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

### Example
Given s = "aba" return true
Given s = "abca" return true // delete c


## 415. Valid Palindrome
https://www.lintcode.com/problem/valid-palindrome

### Description
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

### Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

### Challenge
O(n) time without extra memory.


## 56. Two Sum
https://www.lintcode.com/problem/two-sum

### Description
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

You may assume that each input would have exactly one solution

### Example
numbers=[2, 7, 11, 15], target=9

return [0, 1]

### Challenge
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time


## 521. Remove Duplicate Numbers in Array
https://www.lintcode.com/problem/remove-duplicate-numbers-in-array

### Description
Given an array of integers, remove the duplicate numbers in it.

You should:

Do it in place in the array.
Move the unique numbers to the front of the array.
Return the total number of the unique numbers.
You don't need to keep the original order of the integers.

### Example
Given nums = [1,3,1,4,4,2], you should:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

### Challenge
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.


## 604. Window Sum
https://www.lintcode.com/problem/window-sum

### Description
Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

### Example
For array [1,2,7,8,5], moving window size k = 3.
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]


## 610. Two Sum - Difference equals to target
https://www.lintcode.com/problem/two-sum-difference-equals-to-target

### Description
Given an array of integers, find two numbers that their difference equals to a target value.
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

It's guaranteed there is only one available solution

### Example
Given nums = [2, 7, 15, 24], target = 5
return [1, 2] (7 - 2 = 5)


## 228. Middle of Linked List
https://www.lintcode.com/problem/middle-of-linked-list

### Description
Find the middle node of a linked list.

### Example
Given 1->2->3, return the node with value 2.

Given 1->2, return the node with value 1.

### Challenge
If the linked list is in a data stream, can you find the middle without iterating the linked list again?


## 81. Find Median from Data Stream
https://www.lintcode.com/problem/find-median-from-data-stream

### Description
Numbers keep coming, return the median of numbers at every time a new number added.

### Clarification
What's the definition of Median?

Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]. For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.

### Example
For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].

For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].

For numbers coming list: [2, 20, 100], return [2, 2, 20].

### Challenge
Total run time in O(nlogn).


## 102. Linked List Cycle
https://www.lintcode.com/problem/linked-list-cycle

### Description
Given a linked list, determine if it has a cycle in it.

### Example
Given -21->10->4->5, tail connects to node index 1, return true

### Challenge
#### Follow up:
Can you solve it without using extra space?


## 103. Linked List Cycle II
https://www.lintcode.com/problem/linked-list-cycle-ii

### Description
Given a linked list, return the node where the cycle begins.

If there is no cycle, return null.

### Example
Given -21->10->4->5, tail connects to node index 1，return 10
Explanation：
The last node 5 points to the node whose index is 1, which is 10, so the entrance of the ring is 10

### Challenge
#### Follow up:

Can you solve it without using extra space?


## 380. Intersection of Two Linked Lists
https://www.lintcode.com/problem/intersection-of-two-linked-lists

### Description
Write a program to find the node at which the intersection of two singly linked lists begins.

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.

### Example
The following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

### Challenge
Your code should preferably run in O(n) time and use only O(1) memory.
