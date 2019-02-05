# 9 - Data Structure - Interval, Array, Matrix & Binary Indexed Tree

## Required(4/12)

### Easy  839. Merge Two Sorted Interval Lists
https://www.lintcode.com/problem/merge-two-sorted-interval-lists

#### Description
Merge two sorted (ascending) lists of interval and return it as a new sorted list. The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.

The intervals in the given list do not overlap.
The intervals in different lists may overlap.

#### Example
##### Example1

    Input: list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)]
    Output: [(1,4),(5,6)]
    Explanation:
    (1,2),(2,3),(3,4) --> (1,4)
    (5,6) --> (5,6)

##### Example2

    Input: list1 = [(1,2),(3,4)] and list2 = [(4,5),(6,7)]
    Output: [(1,2),(3,5),(6,7)]
    Explanation:
    (1,2) --> (1,2)
    (3,4),(4,5) --> (3,5)
    (6,7) --> (6,7)

### Easy  547. Intersection of Two Arrays
https://www.lintcode.com/problem/intersection-of-two-arrays

#### Description
Given two arrays, write a function to compute their intersection.

Each element in the result must be unique.
The result can be in any order.

#### Example
##### Example 1:

Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2],
Output: [2].

##### Example 2:

Input: nums1 = [1, 2], nums2 = [2],
Output: [2].

##### Challenge
Can you implement it in three different algorithms?

### Easy  138. Subarray Sum
https://www.lintcode.com/problem/subarray-sum

#### Description
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

There is at least one subarray that it's sum equals to zero.

#### Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

### Easy  64. Merge Sorted Array

### Easy  41. Maximum Subarray
https://www.lintcode.com/problem/maximum-subarray

#### Description
Given an array of integers, find a contiguous subarray which has the largest sum.

The subarray should contain at least one number.

#### Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

#### Challenge
Can you do it in time complexity O(n)?

### Medium  944. Maximum Submatrix
### Medium  931. Median of K Sorted Arrays
### Medium  840. Range Sum Query - Mutable
### Medium  654. Sparse Matrix Multiplication
### Medium  577. Merge K Sorted Interval Lists
### Medium  486. Merge K Sorted Arrays
### Hard  65. Median of two Sorted Arrays

## Optional(2/11)

### Easy  943. Range Sum Query - Immutable
### Easy  165. Merge Two Sorted Lists
### Easy  6. Merge Two Sorted Arrays
### Medium  817. Range Sum Query 2D - Mutable
### Medium  793. Intersection of Arrays
### Medium  665. Range Sum Query 2D - Immutable
### Medium  548. Intersection of Two Arrays II
### Medium  405. Submatrix Sum
### Medium  149. Best Time to Buy and Sell Stock
### Medium  139. Subarray Sum Closest
### Medium  104. Merge K Sorted Lists

## Related(1/11)

### Medium  620. Maximum Subarray IV
### Medium  617. Maximum Average Subarray II
### Medium  191. Maximum Product Subarray
### Medium  151. Best Time to Buy and Sell Stock III
### Medium  150. Best Time to Buy and Sell Stock II
### Medium  45. Maximum Subarray Difference
### Medium  42. Maximum Subarray II
### Hard  404. Subarray Sum II
### Hard  393. Best Time to Buy and Sell Stock IV
### Hard  43. Maximum Subarray III
