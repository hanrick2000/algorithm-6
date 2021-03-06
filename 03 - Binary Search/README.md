# 3 - Binary Search

## Required (10)

### Easy  458. Last Position of Target
https://www.lintcode.com/problem/last-position-of-target/

#### Description

Find the last position of a target number in a sorted array. Return -1 if target does not exist.

#### Example
##### Example 1:

    Input: nums = [1,2,2,4,5,5], target = 2
    Output: 2
##### Example 2:

    Input: nums = [1,2,2,4,5,5], target = 6
    Output: -1


### Medium  585. Maximum Number in Mountain Sequence
https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/

#### Description

Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

#### Example
##### Example 1:

    Input: nums = [1, 2, 4, 8, 6, 3]
    Output: 8
##### Example 2:

    Input: nums = [10, 9, 8, 7],
    Output: 10


### Medium  460. Find K Closest Elements
https://www.lintcode.com/problem/find-k-closest-elements/

#### Description

Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

    1. The value k is a non-negative integer and will always be smaller than the length of the sorted array.
    2. Length of the given array is positive and will not exceed 10^4
    3. Absolute value of elements in the array will not exceed 10^4
​​
#### Example
##### Example 1:

    Input: A = [1, 2, 3], target = 2, k = 3
    Output: [2, 1, 3]
##### Example 2:

    Input: A = [1, 4, 6, 8], target = 3, k = 3
    Output: [4, 1, 6]
#### Challenge
    O(logn + k) time


### Medium  447. Search in a Big Sorted Array
https://www.lintcode.com/problem/search-in-a-big-sorted-array/

#### Description

Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).

Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

    If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.

#### Example
##### Example 1:

    Input: [1, 3, 6, 9, 21, ...], target = 3
    Output: 1
##### Example 2:

    Input: [1, 3, 6, 9, 21, ...], target = 4
    Output: -1

#### Challenge
O(logn) time, n is the first index of the given target number.


### Medium  428. Pow(x, n)
https://www.lintcode.com/problem/powx-n

#### Description
Implement pow(x, n).

You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.

#### Example
Pow(2.1, 3) = 9.261
Pow(0, 1) = 0
Pow(1, 0) = 1

#### Challenge
O(logn) time


### Medium  159. Find Minimum in Rotated Sorted Array
https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/

#### Description

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

    You can assume no duplicate exists in the array.

#### Example
##### Example 1:

    Input：[4, 5, 6, 7, 0, 1, 2]
    Output：0
    Explanation：
    The minimum value in an array is 0.
##### Example 2:

    Input：[2,1]
    Output：1
    Explanation：
    The minimum value in an array is 1.


### Medium  140. Fast Power
https://www.lintcode.com/problem/fast-power

#### Description
Calculate the an % b where a, b and n are all 32bit positive integers.

#### Example
For 231 % 3 = 2

For 1001000 % 1000 = 0

#### Challenge
O(logn)


### Medium  75. Find Peak Element
https://www.lintcode.com/problem/find-peak-element/

#### Description

There is an integer array which has the following features:

* The numbers in adjacent positions are different.
* A[0] < A[1] && A[A.length - 2] > A[A.length - 1].

We define a position P is a peak if:

    A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

* It's guaranteed the array has at least one peak.
* The array may contain multiple peeks, find any of them.
* The array has at least 3 numbers in it.

#### Example
##### Example 1:
  	Input:  [1, 2, 1, 3, 4, 5, 7, 6]
  	Output:  1 or 6

  	Explanation:
  	return the index of peek.

##### Example 2:
  	Input: [1,2,3,4,1]
  	Output:  3

#### Challenge
Time complexity O(logN)


### Medium  74. First Bad Version
https://www.lintcode.com/problem/first-bad-version/

#### Description

The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.

    Please read the annotation in code area to get the correct way to call isBadVersion in different language. For example, Java is SVNRepo.isBadVersion(v)

#### Example
    Given n = 5:

        isBadVersion(3) -> false
        isBadVersion(5) -> true
        isBadVersion(4) -> true

Here we are 100% sure that the 4th version is the first bad version.

#### Challenge
You should call isBadVersion as few as possible.


### Medium  62. Search in Rotated Sorted Array
https://www.lintcode.com/problem/search-in-rotated-sorted-array/

#### Description

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

#### Example
##### Example 1:

    Input: [4, 5, 1, 2, 3] and target=1,
    Output: 2.
##### Example 2:

    Input: [4, 5, 1, 2, 3] and target=0,
    Output: -1.

#### Challenge
O(logN) time


## Optional (10)

### Easy  462. Total Occurrence of Target
https://www.lintcode.com/problem/total-occurrence-of-target/

#### Description

Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.

#### Example
##### Example1:

    Input: [1, 3, 3, 4, 5] and target = 3,
    Output: 2.
##### Example2:

    Input: [2, 2, 3, 4, 6] and target = 4,
    Output: 1.
##### Example3:

    Input: [1, 2, 3, 4, 5] and target = 6,
    Output: 0.

#### Challenge
Time complexity in O(logn)


### Easy  459. Closest Number in Sorted Array
https://www.lintcode.com/problem/closest-number-in-sorted-array/

#### Description

Given a target number and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to the given target.

Return -1 if there is no element in the array.

    There can be duplicate elements in the array, and we can return any of the indices with same value.

#### Example
##### Example 1:

    Input: [1, 2, 3] , target = 2
    Output: 1.
##### Example 2:

    Input: [1, 4, 6], target = 3
    Output: 1.
##### Example 3:

    Input: [1, 4, 6], target = 5,
    Output: 1 or 2.

#### Challenge
O(logn) time complexity.


### Easy  235. Prime Factorization
https://www.lintcode.com/problem/prime-factorization/

#### Description

Prime factorize a given integer.

    You should sort the factors in ascending order.

#### Example
##### Example 1:

    Input: 10
    Output: [2, 5]
##### Example 2:

    Input: 660
    Output: [2, 2, 3, 5, 11]


### Easy  254. Drop Eggs
https://www.lintcode.com/problem/drop-eggs/

#### Description

There is a building of n floors. If an egg drops from the k th floor or above, it will break. If it's dropped from any floor below, it will not break.

You're given two eggs, Find k while minimize the number of drops for the worst case. Return the number of drops in the worst case.

#### Clarification
For n = 10, a naive way to find k is drop egg from 1st floor, 2nd floor ... kth floor. But in this worst case (k = 10), you have to drop 10 times.

Notice that you have two eggs, so you can drop at 4th, 7th & 9th floor, in the worst case (for example, k = 9) you have to drop 4 times.

#### Example
##### Example 1:

    Input: 100
    Output: 14
##### Example 2:

    Input: 10
    Output: 4


### Easy  28. Search a 2D Matrix
https://www.lintcode.com/problem/search-a-2d-matrix/

#### Description

Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.

#### Example
##### Example 1:
  	Input:  [[5]],2
  	Output: false

  	Explanation:
  	false if not included.

##### Example 2:
  	Input:  [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
  ],3
  	Output: true

  	Explanation:
  	return true if included.

#### Challenge
O(log(n) + log(m)) time


### Easy  14. First Position of Target
https://www.lintcode.com/problem/first-position-of-target

#### Description
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

#### Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

#### Challenge
If the count of numbers is bigger than 2^32, can your code work properly?


### Medium  414. Divide Two Integers
https://www.lintcode.com/problem/divide-two-integers/

### Medium  61. Search for a Range
https://www.lintcode.com/problem/search-for-a-range/

### Medium  38. Search a 2D Matrix II
https://www.lintcode.com/problem/search-a-2d-matrix-ii

#### Description
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.

#### Example
Consider the following matrix:

[
  [1, 3, 5, 7],
  [2, 4, 7, 8],
  [3, 5, 9, 10]
]
Given target = 3, return 2.

#### Challenge
O(m+n) time and O(1) extra space


### Hard  600. Smallest Rectangle Enclosing Black Pixels
https://www.lintcode.com/problem/smallest-rectangle-enclosing-black-pixels/

## Related (8)

### Easy  457. Classical Binary Search
https://www.lintcode.com/problem/classical-binary-search

#### Description
Find any position of a target number in a sorted array. Return -1 if target does not exist.

#### Example
Given [1, 2, 2, 4, 5, 5].

For target = 2, return 1 or 2.

For target = 5, return 4 or 5.

For target = 6, return -1.

#### Challenge
O(logn) time


### Easy  141. Sqrt(x)
https://www.lintcode.com/problem/sqrtx/
https://leetcode.com/problems/sqrtx/

#### Description

Implement int sqrt(int x).

Compute and return the square root of x.

#### Example
##### Example 1:
  	Input:  0
  	Output: 0


##### Example 2:
  	Input:  3
  	Output: 1

  	Explanation:
  	return the largest integer y that y*y <= x.

##### Example 3:
  	Input:  4
  	Output: 2

#### Challenge
O(log(x))


### Medium  617. Maximum Average Subarray II
https://www.lintcode.com/problem/maximum-average-subarray-ii/

#### Description

Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.

    It's guaranteed that the size of the array is greater or equal to k.

#### Example
##### Example 1:

    Input:
    [1,12,-5,-6,50,3]
    3
    Output:
    15.667
    Explanation:
     (-6 + 50 + 3) / 3 = 15.667
##### Example 2:

    Input:
    [5]
    1
    Output:
    5.000

### Medium  586. Sqrt(x) II
https://www.lintcode.com/problem/sqrtx-ii/

### Medium  160. Find Minimum in Rotated Sorted Array II
https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array-ii/
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/submissions/

#### Description
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

    The array may contain duplicates.

#### Example
##### Example 1:

    Input :[2,1]
    Output : 1.
##### Example 2:

    Input :[4,4,5,6,7,0,1,2]
    Output : 0.

##### Example 3:

    Input: [2,2,2,0,1]
    Output: 0
#### Note:

    This is a follow up problem to Find Minimum in Rotated Sorted Array.
    Would allow duplicates affect the run-time complexity? How and why?

### Medium  63. Search in Rotated Sorted Array II
https://www.lintcode.com/problem/search-in-rotated-sorted-array-ii/

#### Description
Follow up for Search in Rotated Sorted Array:

What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

#### Example
##### Example 1:

    Input:
    []
    1
    Output:
    false
##### Example 2:

    Input:
    [3,4,4,5,7,0,1,2]
    4
    Output:
    true

### Hard  437. Copy Books
https://www.lintcode.com/problem/copy-books/

#### Description

Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Return the shortest time that the slowest copier spends.

    The sum of book pages is less than or equal to 2147483647

#### Example
##### Example 1:

    Input: pages = [3, 2, 4], k = 2
    Output: 5
    Explanation:
        First person spends 5 minutes to copy book 1 and book 2.
        Second person spends 4 minutes to copy book 3.
##### Example 2:

    Input: pages = [3, 2, 4], k = 3
    Output: 4
    Explanation: Each person copies one of the books.
#### Challenge
O(nk) time

### Hard  183. Wood Cut
https://www.lintcode.com/problem/wood-cut/


## ----------------------------------------------------------------

### Easy 868. Maximum Average Subarray

#### Description
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. You need to output the maximum average value.

    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].

#### Example
##### Example1

    Input:  nums = [1,12,-5,-6,50,3] and k = 4
    Output: 12.75
    Explanation:
    Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
##### Example2

    Input:  nums = [4,2,1,3,3] and k = 2
    Output: 3.00
    Explanation:
    Maximum average is (3+3)/2 = 6/2 = 3.00
