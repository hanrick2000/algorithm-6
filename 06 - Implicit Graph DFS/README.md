# 6 - Implicit Graph DFS

## Required (10)

### Medium 680. Split String
https://www.lintcode.com/problem/split-string

#### Description
Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.

#### Example
Given the string "123"
return [["1","2","3"],["12","3"],["1","23"]]


### Medium  425. Letter Combinations of a Phone Number
https://www.lintcode.com/problem/letter-combinations-of-a-phone-number/

#### Description
Given a digit string excluded 01, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

![Cellphone](https://github.com/porrychen/algorithm/blob/master/7%20-%20Permutation-based%20&%20Graph-based%20DFS/425-Telephone-keypad.png?raw=true)

Although the above answer is in lexicographical order, your answer could be in any order you want.

#### Example
    Given "23"

    Return
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


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


### Medium  33. N-Queens
https://www.lintcode.com/problem/n-queens

#### Description
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

#### Example
There exist two distinct solutions to the 4-queens puzzle:

        [
          // Solution 1
          [".Q..",
           "...Q",
           "Q...",
           "..Q."
          ],
          // Solution 2
          ["..Q.",
           "Q...",
           "...Q",
           ".Q.."
          ]
        ]

#### Challenge
    Can you do it without recursion?


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

### Medium  15. Permutations
https://www.lintcode.com/problem/permutations

#### Description
Given a list of numbers, return all possible permutations.

You can assume that there is no duplicate numbers in the list.

#### Example
For nums = [1,2,3], the permutations are:

    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

#### Challenge
Do it without recursion.


### Hard  829. Word Pattern II
https://www.lintcode.com/problem/word-pattern-ii

#### Description
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)

You may assume both pattern and str contains only lowercase letters.

#### Example
Given pattern = "abab", str = "redblueredblue", return true.
Given pattern = "aaaa", str = "asdasdasdasd", return true.
Given pattern = "aabb", str = "xyzabcxzyabc", return false.


### Hard  121. Word Ladder II
https://www.lintcode.com/problem/word-ladder-ii

#### Description
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
All words have the same length.
All words contain only lowercase alphabetic characters.

#### Example
Given:
    start = "hit"
    end = "cog"
    dict = ["hot","dot","dog","lot","log"]

Return
    [
      ["hit","hot","dot","dog","cog"],
      ["hit","hot","lot","log","cog"]
    ]


## Optional (7)

### Medium  652. Factorization
https://www.lintcode.com/problem/factorization/

### Medium  570. Find the Missing Number II
https://www.lintcode.com/problem/find-the-missing-number-ii/

### Medium  426. Restore IP Addresses
https://www.lintcode.com/problem/restore-ip-addresses/

### Medium  427. Generate Parentheses
https://www.lintcode.com/problem/generate-parentheses/

### Medium  152. Combinations
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

### Medium  16. Permutations II
https://www.lintcode.com/problem/permutations-ii

#### Description
Given a list of numbers with duplicate number in it. Find all unique permutations.

#### Example
For numbers [1,2,2] the unique permutations are:

    [
      [1,2,2],
      [2,1,2],
      [2,2,1]
    ]

#### Challenge
Using recursion to do it is acceptable. If you can do it without recursion, that would be great!


### Hard    780. Remove Invalid Parentheses
https://www.lintcode.com/problem/remove-invalid-parentheses/


## Related (1)

### Medium  196. Missing Number
https://www.lintcode.com/problem/missing-number/
