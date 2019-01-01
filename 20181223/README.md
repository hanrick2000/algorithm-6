# 20181223

## 594. strStr II
http://www.lintcode.com/problem/strstr-ii/

### Description
Implement strStr function in O(n + m) time.

strStr return the first index of the target string in a source string. The length of the target string is m and the length of the source string is n.
If target does not exist in source, just return -1.

#### Example
Given source = abcdef, target = bcd, return 1.


## 14. First Position of Target
https://www.lintcode.com/problem/first-position-of-target

### Description
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

#### Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

#### Challenge
If the count of numbers is bigger than 2^32, can your code work properly?


## 235. Prime Factorization
https://www.lintcode.com/problem/prime-factorization

### Description
Prime factorize a given integer.

You should sort the factors in ascending order.

### Example
Given 10, return [2, 5].

Given 660, return [2, 2, 3, 5, 11].


## 457. Classical Binary Search
https://www.lintcode.com/problem/classical-binary-search

### Description
Find any position of a target number in a sorted array. Return -1 if target does not exist.

### Example
Given [1, 2, 2, 4, 5, 5].

For target = 2, return 1 or 2.

For target = 5, return 4 or 5.

For target = 6, return -1.

### Challenge
O(logn) time


## 39. Recover Rotated Sorted Array
https://www.lintcode.com/problem/recover-rotated-sorted-array

### Description
Given a rotated sorted array, recover it to sorted array in-place.

### Clarification
What is rotated array?
For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]

### Example
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

### Challenge
In-place, O(1) extra space and O(n) time.


## 38. Search a 2D Matrix II
https://www.lintcode.com/problem/search-a-2d-matrix-ii

### Description
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.

### Example
Consider the following matrix:

[
  [1, 3, 5, 7],
  [2, 4, 7, 8],
  [3, 5, 9, 10]
]
Given target = 3, return 2.

### Challenge
O(m+n) time and O(1) extra space


## 428. Pow(x, n)
https://www.lintcode.com/problem/powx-n

### Description
Implement pow(x, n).

You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.

### Example
Pow(2.1, 3) = 9.261
Pow(0, 1) = 0
Pow(1, 0) = 1

### Challenge
O(logn) time


## 140. Fast Power
https://www.lintcode.com/problem/fast-power

### Description
Calculate the an % b where a, b and n are all 32bit positive integers.

### Example
For 231 % 3 = 2

For 1001000 % 1000 = 0

### Challenge
O(logn)


## 845. Greatest Common Divisor
https://www.lintcode.com/problem/greatest-common-divisor

### Description
Given two numbers, number a and number b. Find the greatest common divisor of the given two numbers.

In mathematics, the greatest common divisor (gcd) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers.

### Example
Given a = 10, b = 15, return 5.
Given a = 15, b = 30, return 15.
