# 20190110

## 52. Next Permutation
https://www.lintcode.com/problem/next-permutation

### Description
Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

The list may contains duplicate integers.

### Example
For [1,3,2,3], the next permutation is [1,3,3,2]

For [4,3,2,1], the next permutation is [1,2,3,4]


## 190. Next Permutation II
https://www.lintcode.com/problem/next-permutation-ii

### Description
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

### Example
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

### Challenge
The replacement must be in-place, do not allocate extra memory.

## 197. Permutation Index
https://www.lintcode.com/problem/permutation-index

### Description
Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.

### Example
Given [1,2,4], return 1.


## 955. Implement Queue by Circular Array
https://www.lintcode.com/problem/implement-queue-by-circular-array

### Description
Implement queue by circulant array. You need to support the following methods:

CircularQueue(n): initialize a circular array with size n to store elements
boolean isFull(): return true if the array is full
boolean isEmpty(): return true if there is no element in the array
void enqueue(element): add an element to the queue
int dequeue(): pop an element from the queue
it's guaranteed in the test cases we won't call enqueue if it's full and we also won't call dequeue if it's empty. So it's ok to raise exception in scenarios described above.

### Example
    CircularQueue(5)
    isFull()   => false
    isEmpty() => true
    enqueue(1)
    dequeue()  => 1


## 44. Minimum Subarray
https://www.lintcode.com/problem/minimum-subarray

### Description
Given an array of integers, find the subarray with smallest sum.

Return the sum of the subarray.

The subarray should contain one integer at least.

### Example
For [1, -1, -2, 1], return -3.

## 65. Median of two Sorted Arrays
https://www.lintcode.com/problem/median-of-two-sorted-arrays

### Description
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

### Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.

Given A=[1,2,3] and B=[4,5], the median is 3.

### Challenge
The overall run time complexity should be O(log (m+n)).


## 30. Insert Interval
https://www.lintcode.com/problem/insert-interval

### Description
Given a non-overlapping interval list which is sorted by start point.

Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).

### Example
Insert (2, 5) into [(1,2), (5,9)], we get [(1,9)].

Insert (3, 4) into [(1,2), (5,9)], we get [(1,2), (3,4), (5,9)].


## 156. Merge Intervals
https://www.lintcode.com/problem/merge-intervals

### Description
Given a collection of intervals, merge all overlapping intervals.

### Example
Given intervals => merged intervals:

    [                     [
      (1, 3),               (1, 6),
      (2, 6),      =>       (8, 10),
      (8, 10),              (15, 18)
      (15, 18)            ]
    ]

### Challenge
O(n log n) time and O(1) extra space.


----
> ## 15. Permutations (deleted on January 20, 2019)
> ## 16. Permutations II (deleted on January 20, 2019)
> ## 494. Implement Stack by Two Queues (deleted on January 22, 2019)
> ## 495. Implement Stack (deleted on January 23, 2019)
> ## 104. Merge K Sorted Lists (deleted on January 30, 2019)
> ## 41. Maximum Subarray (deleted on February 2, 2019)
> ## 138. Subarray Sum (deleted on February 3, 2019)
> ## 128. Hash Function (deleted on May 31, 2019)
> ## 129. Rehashing (deleted on May 31, 2019)
> ## 130. Heapify (deleted on May 31, 2019)
> ## 224. Implement Three Stacks by Single Array (deleted on May 31, 2019)
