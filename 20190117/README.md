# 20190117

## 365. Count 1 in Binary
https://www.lintcode.com/problem/count-1-in-binary

### Description
Count how many 1 in binary representation of a 32-bit integer.

### Example
Given 32, return 1

Given 5, return 2

Given 1023, return 9

### Challenge
If the integer is n bits with m 1 bits. Can you do it in O(m) time?


## 179. Update Bits
https://www.lintcode.com/problem/update-bits

#### Description
Given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M (e g , M becomes a substring of N start from i to j)

In the function, the numbers N and M will given in decimal, you should also return a decimal number.

#### Clarification
You can assume that the bits j through i have enough space to fit all of M. That is, if M=10011， you can assume that there are at least 5 bits between j and i. You would not, for example, have j=3 and i=2, because M could not fully fit between bit 3 and bit 2.

#### Example
Given N=(10000000000)2, M=(10101)2, i=2, j=6

return N=(10001010100)2

#### Challenge
Minimum number of operations?


### Medium 136. Palindrome Partitioning
https://www.lintcode.com/problem/palindrome-partitioning

#### Description
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

#### Example
Given s = "aab", return:

    [
      ["aa","b"],
      ["a","a","b"]
    ]


### Medium  10. String Permutation II
https://www.lintcode.com/problem/string-permutation-ii

#### Description
Given a string, find all permutations of it without duplicates.

#### Example
Given "abb", return ["abb", "bab", "bba"].

Given "aabb", return ["aabb", "abab", "baba", "bbaa", "abba", "baab"].

### Medium  34. N-Queens II
https://www.lintcode.com/problem/n-queens-ii

#### Description
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

#### Example
For n=4, there are 2 distinct solutions.


### Hard  132. Word Search II
https://www.lintcode.com/problem/word-search-ii

#### Description
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. One character only be used once in one word. No same word in dictionary

#### Example
Given matrix:
    doaf
    agai
    dcan
and dictionary:

    {"dog", "dad", "dgdg", "can", "again"}

    return {"dog", "dad", "can", "again"}

    dog:
    doaf
    agai
    dcan
    dad:

    doaf
    agai
    dcan
    can:

    doaf
    agai
    dcan
    again:

    doaf
    agai
    dcan

#### Challenge
Using trie to implement your algorithm.


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


### Easy  41. Maximum Subarray
https://www.lintcode.com/problem/maximum-subarray

#### Description
Given an array of integers, find a contiguous subarray which has the largest sum.

The subarray should contain at least one number.

#### Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

#### Challenge
Can you do it in time complexity O(n)?


----
> ## 486. Merge K Sorted Arrays (deleted on May 31, 2019)
