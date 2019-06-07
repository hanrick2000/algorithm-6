# 8 - Memoization Search & Dynamic Programming

## Required (6)

### Medium 683. Word Break III
### Medium 109. Triangle
### Medium 107. Word Break

### Hard   582. Word Break II
https://www.lintcode.com/problem/word-break-ii

#### Description
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

#### Example
Gieve s = lintcode,
dict = ["de", "ding", "co", "code", "lint"].

A solution is ["lint code", "lint co de"].


### Hard   192. Wildcard Matching
https://www.lintcode.com/problem/wildcard-matching

#### Description
Implement wildcard pattern matching with support for '?' and '\*'.

'?' Matches any single character.
'\*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

#### Example
    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "\*") → true
    isMatch("aa", "a*") → true
    isMatch("ab", "?\*") → true
    isMatch("aab", "c*a*b") → false

### Hard   154. Regular Expression Matching
https://www.lintcode.com/problem/regular-expression-matching

#### Description
Implement regular expression matching with support for '.' and '\*'.

'.' Matches any single character.
'\*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


The function prototype should be:

bool isMatch(string s, string p)

#### Example
    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "a*") → true
    isMatch("aa", ".\*") → true
    isMatch("ab", ".\*") → true
    isMatch("aab", "c*a*b") → true


## Optional (6)

### Medium 190. Next Permutation II
https://www.lintcode.com/problem/next-permutation-ii

#### Description
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

#### Example
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

#### Challenge
The replacement must be in-place, do not allocate extra memory.


### Medium 198. Permutation Index II

### Medium 197. Permutation Index
https://www.lintcode.com/problem/permutation-index

#### Description
Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.

#### Example
Given [1,2,4], return 1.


### Medium 52. Next Permutation
https://www.lintcode.com/problem/next-permutation

### Description
Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

The list may contains duplicate integers.

### Example
For [1,3,2,3], the next permutation is [1,3,3,2]

For [4,3,2,1], the next permutation is [1,2,3,4]


### Medium 51. Previous Permutation
### Hard   634. Word Squares

## Related (3)

### Easy   828. Word Pattern
### Easy   211. String Permutation
### Medium 123. Word Search