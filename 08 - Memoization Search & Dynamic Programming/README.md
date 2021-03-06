# 8 - Memoization Search & Dynamic Programming

## Required (6)

### Medium 683. Word Break III
https://www.lintcode.com/problem/word-break-iii/

#### Description

Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

    Ignore case

#### Example
##### Example1

    Input:
    "CatMat"
    ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
    Output: 3
    Explanation:
    we can form 3 sentences, as follows:
    "CatMat" = "Cat" + "Mat"
    "CatMat" = "Ca" + "tM" + "at"
    "CatMat" = "C" + "at" + "Mat"

#### Example2

    Input:
    "a"
    []
    Output: 0


### Medium 109. Triangle
https://www.lintcode.com/problem/triangle/

#### Description

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

#### Example
##### Example 1:

    Input the following triangle:
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    Output: 11
    Explanation: The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

#### Example 2:

    Input the following triangle:
    [
         [2],
        [3,2],
       [6,5,7],
      [4,4,8,1]
    ]
    Output: 12
    Explanation: The minimum path sum from top to bottom is 12 (i.e., 2 + 2 + 7 + 1 = 12).


### Medium 107. Word Break
https://www.lintcode.com/problem/word-break/

#### Description

Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.

#### Example
##### Example 1:
	Input:  "lintcode", ["lint", "code"]
	Output:  true

##### Example 2:
	Input: "a", ["a"]
	Output:  true


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
https://www.lintcode.com/problem/permutation-index-ii/

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
https://www.lintcode.com/problem/previous-permutation/

### Hard   634. Word Squares
https://www.lintcode.com/problem/word-squares/

## Related (3)

### Easy   828. Word Pattern
https://www.lintcode.com/problem/word-pattern/
https://leetcode.com/problems/word-pattern/

#### Description

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

    You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

#### Example
##### Example1

    Input:  pattern = "abba" and str = "dog cat cat dog"
    Output: true
    Explanation:
    The pattern of str is abba
##### Example2

    Input:  pattern = "abba" and str = "dog cat cat fish"
    Output: false
    Explanation:
    The pattern of str is abbc
##### Example3

    Input:  pattern = "aaaa" and str = "dog cat cat dog"
    Output: false
    Explanation:
    The pattern of str is abba
##### Example4

    Input:  pattern = "abba" and str = "dog cat cat fish"
    Output: false
    Explanation:
    The pattern of str is abbc


### Easy   211. String Permutation
https://www.lintcode.com/problem/string-permutation/

#### Description

Given two strings, write a method to decide if one is a permutation of the other.

#### Example
##### Example 1:
  	Input:  "abcd", "bcad"
  	Output:  True


##### Example 2:
  	Input: "aac", "abc"
  	Output:  False


### Medium 123. Word Search
https://www.lintcode.com/problem/word-search/
