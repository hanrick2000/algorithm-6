# 20190104

## 463. Sort Integers
https://www.lintcode.com/problem/sort-integers

### Description
Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.

### Example
Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].


## 464. Sort Integers II
https://www.lintcode.com/problem/sort-integers-ii

### Description
Given an integer array, sort it in ascending order. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

### Example
Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].


## 5. Kth Largest Element
https://www.lintcode.com/problem/kth-largest-element

### Description
Find K-th largest element in an array.

You can swap elements in the array

### Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

### Challenge
O(n) time, O(1) extra memory.


## 148. Sort Colors
https://www.lintcode.com/problem/sort-colors

### Description
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

You are not suppose to use the library's sort function for this problem.
You should do it in-place (sort numbers in the original array).

### Example
Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].

### Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
