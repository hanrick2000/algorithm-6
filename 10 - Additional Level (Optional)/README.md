# 10 - Additional Level (Optional)

## Required(12)

### Easy  839. Merge Two Sorted Interval Lists
https://www.lintcode.com/problem/merge-two-sorted-interval-lists
https://leetcode.com/problems/merge-intervals/

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
https://leetcode.com/problems/intersection-of-two-arrays/

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
https://www.lintcode.com/problem/merge-sorted-array/
https://leetcode.com/problems/merge-sorted-array/

#### Description

Given two sorted integer arrays A and B, merge B into A as one sorted array.

You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

#### Example
##### Example 1:

    Input：[1, 2, 3] 3  [4,5]  2
    Output：[1,2,3,4,5]
    Explanation:
    After merge, A will be filled as [1, 2, 3, 4, 5]

##### Example 2:

    Input：[1,2,5] 3 [3,4] 2
    Output：[1,2,3,4,5]
    Explanation:
    After merge, A will be filled as [1, 2, 3, 4, 5]


### Easy  41. Maximum Subarray
https://www.lintcode.com/problem/maximum-subarray
https://leetcode.com/problems/maximum-subarray/

#### Description
Given an array of integers, find a contiguous subarray which has the largest sum.

The subarray should contain at least one number.

#### Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

#### Challenge
Can you do it in time complexity O(n)?


### Medium 944. Maximum Submatrix
https://www.lintcode.com/problem/maximum-submatrix/

#### Description

Given an n x n matrix of positive and negative integers, find the submatrix with the largest possible sum.

#### Example
##### Example1

    Input:  
    matrix = [
        [1,3,-1],
        [2,3,-2],
        [-1,-2,-3]
    ]
    Output: 9
    Explanation:
    the submatrix with the largest possible sum is:
    [
        [1,3],
        [2,3]
    ]

##### Example2

    Input:  
    matrix = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]
    Output: 9
    Explanation:
    the submatrix with the largest possible sum is:
    [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]


### Medium 840. Range Sum Query - Mutable
https://www.lintcode.com/problem/range-sum-query-mutable/

#### Description

Given an integer array nums, and then you need to implement two functions:

* update(i, val) Modify the element whose index is i to val.
* sumRange(l, r) Return the sum of elements whose indexes are in range of [l, r][l,r].

  1. The array is only modifiable by the update function.
  2. You may assume the number of calls to update and sumRange function is distributed evenly.

#### Example
##### Example 1:

    Input:
      nums = [1, 3, 5]
      sumRange(0, 2)
      update(1, 2)
      sumRange(0, 2)
    Output:
      9
      8

#### Example 2:

    Input:
      nums = [0, 9, 5, 7, 3]
      sumRange(4, 4)
      sumRange(2, 4)
      update(4, 5)
      update(1, 7)
      update(0, 8)
      sumRange(1, 2)
    Output:
      3
      15
      12


### Medium 654. Sparse Matrix Multiplication
https://www.lintcode.com/problem/sparse-matrix-multiplication/

#### Description

Given two Sparse Matrix A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

#### Example
##### Example1

    Input:
    [[1,0,0],[-1,0,3]]
    [[7,0,0],[0,0,0],[0,0,1]]
    Output:
    [[7,0,0],[-7,0,3]]
    Explanation:
    A = [
      [ 1, 0, 0],
      [-1, 0, 3]
    ]

    B = [
      [ 7, 0, 0 ],
      [ 0, 0, 0 ],
      [ 0, 0, 1 ]
    ]

         |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
    AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                      | 0 0 1 |
##### Example2

    Input:
    [[1,0],[0,1]]
    [[0,1],[1,0]]
    Output:
    [[0,1],[1,0]]


### Medium 577. Merge K Sorted Interval Lists
https://www.lintcode.com/problem/merge-k-sorted-interval-lists/

#### Description

Merge K sorted interval lists into one sorted interval list. You need to merge overlapping intervals too.

#### Example
##### Example1

    Input: [
      [(1,3),(4,7),(6,8)],
      [(1,2),(9,10)]
    ]
    Output: [(1,3),(4,8),(9,10)]

##### Example2

    Input: [
      [(1,2),(5,6)],
      [(3,4),(7,8)]
    ]
    Output: [(1,2),(3,4),(5,6),(7,8)]


### Medium 486. Merge K Sorted Arrays
https://www.lintcode.com/problem/merge-k-sorted-arrays/

### Hard 931. Median of K Sorted Arrays
https://www.lintcode.com/problem/median-of-k-sorted-arrays/

#### Description

There are k sorted arrays nums. Find the median of the given k sorted arrays.

    * The length of the given arrays may not equal to each other.
    * The elements of the given arrays are all positive number.
    * Return 0 if there are no elements in the array.
    * In order to ensure time complexity, the program will be executed repeatedly.

#### Example
##### Example 1:

    Input:
    [[1],[2],[3]]
    Output:
    2.00

##### Example 2:

    Input:
    [[1,1,2],[2,4,8],[3,7,10,20]]
    Output:
    3.50

### Hard 65. Median of two Sorted Arrays
https://www.lintcode.com/problem/median-of-two-sorted-arrays

#### Description
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

#### Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.

Given A=[1,2,3] and B=[4,5], the median is 3.

#### Challenge
The overall run time complexity should be O(log (m+n)).


## Optional(11)

### Easy 943. Range Sum Query - Immutable
https://www.lintcode.com/problem/range-sum-query-immutable/
https://leetcode.com/problems/range-sum-query-immutable/

#### Description

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

    1. You may assume that the array does not change.
    2. There are many calls to sumRange function.

#### Example
##### Example1

Input: nums = [-2, 0, 3, -5, 2, -1]
    sumRange(0, 2)
    sumRange(2, 5)
    sumRange(0, 5)
    Output:
    1
    -1
    -3
    Explanation:
    sumRange(0, 2) -> (-2) + 0 + 3 = 1
    sumRange(2, 5) -> 3 + (-5) + 2 + (-1) = -1
    sumRange(0, 5) -> (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
##### Example2

    Input:
    nums = [-4, -5]
    sumRange(0, 0)
    sumRange(1, 1)
    sumRange(0, 1)
    sumRange(1, 1)
    sumRange(0, 0)
    Output:
    -4
    -5
    -9
    -5
    -4
    Explanation:
    sumRange(0, 0) -> -4
    sumRange(1, 1) -> -5
    sumRange(0, 1) -> (-4) + (-5) = -9
    sumRange(1, 1) -> -5
    sumRange(0, 0) -> -4


### Easy 165. Merge Two Sorted Lists
https://www.lintcode.com/problem/merge-two-sorted-lists/
https://leetcode.com/problems/merge-two-sorted-lists/

#### Description

Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.

#### Example
##### Example 1:
  	Input: list1 = null, list2 = 0->3->3->null
  	Output: 0->3->3->null

##### Example 2:
	Input:  list1 =  1->3->8->11->15->null, list2 = 2->null
	Output: 1->2->3->8->11->15->null


### Easy 6. Merge Two Sorted Arrays
https://www.lintcode.com/problem/merge-two-sorted-arrays/

#### Description

Merge two given sorted ascending integer array A and B into a new sorted integer array.

#### Example
##### Example 1:

    Input:  A=[1], B=[1]
    Output: [1,1]
    Explanation:  return array merged.
##### Example 2:

    Input:  A=[1,2,3,4], B=[2,4,5,6]
    Output: [1,2,2,3,4,4,5,6]
    Explanation: return array merged.
#### Challenge
How can you optimize your algorithm if one array is very large and the other is very small?


### Medium 817. Range Sum Query 2D - Mutable
https://www.lintcode.com/problem/range-sum-query-2d-mutable/

### Medium 793. Intersection of Arrays
https://www.lintcode.com/problem/intersection-of-arrays/

### Medium 665. Range Sum Query 2D - Immutable
https://www.lintcode.com/problem/range-sum-query-2d-immutable/

### Medium 548. Intersection of Two Arrays II
https://www.lintcode.com/problem/intersection-of-two-arrays-ii/

### Medium 405. Submatrix Sum
https://www.lintcode.com/problem/submatrix-sum/

### Medium 149. Best Time to Buy and Sell Stock
https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock/

### Medium 139. Subarray Sum Closest
https://www.lintcode.com/problem/subarray-sum-closest/

### Medium 104. Merge K Sorted Lists
https://www.lintcode.com/problem/merge-k-sorted-lists/

## Related(11)

### Easy41. Maximum Subarray
https://www.lintcode.com/problem/maximum-subarray/

### Medium 620. Maximum Subarray IV
https://www.lintcode.com/problem/maximum-subarray-iv/

### Medium 617. Maximum Average Subarray II
https://www.lintcode.com/problem/maximum-average-subarray-ii/

### Medium 404. Subarray Sum II
https://www.lintcode.com/problem/subarray-sum-ii/

### Medium 393. Best Time to Buy and Sell Stock IV
https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iv/?

### Medium 191. Maximum Product Subarray
https://www.lintcode.com/problem/maximum-product-subarray/

### Medium 151. Best Time to Buy and Sell Stock III
https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iii/

### Medium 150. Best Time to Buy and Sell Stock II
https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-ii/

### Medium 45. Maximum Subarray Difference
https://www.lintcode.com/problem/maximum-subarray-difference/

### Medium 42. Maximum Subarray II
https://www.lintcode.com/problem/maximum-subarray-ii/?_from=ladder&&fromId=1

### Hard 43. Maximum Subarray III
https://www.lintcode.com/problem/maximum-subarray-iii/


## ==============================

### Easy 838. Subarray Sum Equals K
https://www.lintcode.com/problem/subarray-sum-equals-k/
https://leetcode.com/problems/subarray-sum-equals-k/

#### Description

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

#### Example
##### Example1

    Input: nums = [1,1,1] and k = 2
    Output: 2
    Explanation:
    subarray [0,1] and [1,2]
##### Example2

    Input: nums = [2,1,-1,1,2] and k = 3
    Output: 4
    Explanation:
    subarray [0,1], [1,4], [0,3] and [3,4]


### Medium 36. Reverse Linked List II

#### Description

Reverse a linked list from position m to n.

    Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.

#### Example
##### Example 1:

    Input: 1->2->3->4->5->NULL, m = 2 and n = 4,
    Output: 1->4->3->2->5->NULL.
##### Example 2:

    Input: 1->2->3->4->NULL, m = 2 and n = 3,
    Output: 1->3->2->4->NULL.
#### Challenge
Reverse it in-place and in one-pass


### Easy 452. Remove Linked List Elements

#### Description

Remove all elements from a linked list of integers that have value val.

#### Example
##### Example 1:

    Input: head = 1->2->3->3->4->5->3->null, val = 3
    Output: 1->2->4->5->null
##### Example 2:

    Input: head = 1->1->null, val = 1
    Output: null
