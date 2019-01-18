# 6 - Combination-based DFS

## Required

### Medium 680. Split String
https://www.lintcode.com/problem/split-string

#### Description
Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.

#### Example
Given the string "123"
return [["1","2","3"],["12","3"],["1","23"]]

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

### Medium 153. Combination Sum II
https://www.lintcode.com/problem/combination-sum-ii

#### Description
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.

#### Example
Given candidate set [10,1,6,7,2,1,5] and target 8,

A solution set is:

    [
      [1,7],
      [1,2,5],
      [2,6],
      [1,1,6]
    ]

### Medium 152. Combinations
https://www.lintcode.com/problem/combinations

#### Description
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You don't need to care the order of combinations, but you should make sure the numbers in a combination are sorted.

#### Example
Given n = 4 and k = 2, a solution is:

    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4]
    ]

### Medium 135. Combination Sum
https://www.lintcode.com/problem/combination-sum/

#### Description
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.

#### Example
Given candidate set [2,3,6,7] and target 7, a solution set is:

    [7]
    [2, 2, 3]

### Medium 18. Subsets II
https://www.lintcode.com/problem/subsets-ii

#### Description
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.

#### Example
Input: [1,2,2]
Output:

    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]

#### Challenge
Can you do it in both recursively and iteratively?

### Medium 17. Subsets
https://www.lintcode.com/problem/subsets

#### Description
Given a set of distinct integers, return all possible subsets.

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

#### Example
If S = [1,2,3], a solution is:

    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]

#### Challenge
Can you do it in both recursively and iteratively?

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
### Hard   154. Regular Expression Matching


## Optional

### Medium  652. Factorization
### Medium  570. Find the Missing Number II
### Medium  426. Restore IP Addresses
### Medium  427. Generate Parentheses
### Hard    780. Remove Invalid Parentheses

## Related

### Medium  683. Word Break III
### Medium  196. Missing Number
### Medium  107. Word Break
### Medium  108. Palindrome Partitioning II
