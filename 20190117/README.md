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


## 486. Merge K Sorted Arrays
https://www.lintcode.com/problem/merge-k-sorted-arrays

### Description
Given k sorted integer arrays, merge them into one sorted array.

### Example
Given 3 sorted arrays:

    [
      [1, 3, 5, 7],
      [2, 4, 6],
      [0, 8, 9, 10, 11]
    ]
return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].

### Challenge
Do it in O(N log k).

N is the total number of integers.
k is the number of arrays.

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
