# 9 - 4 Key Points of DP and Coordinate DP

## Required (8)

### Easy   115. Unique Paths II
https://www.lintcode.com/problem/unique-paths-ii

#### Description

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

m and n will be at most 100.

#### Example
##### Example 1:
	Input: [[0]]
	Output: 1

##### Example 2:
	Input:  [[0,0,0],[0,1,0],[0,0,0]]
	Output: 2

	Explanation:
	Only 2 different path.


### Easy   114. Unique Paths
https://www.lintcode.com/problem/unique-paths
https://leetcode.com/problems/unique-paths/

#### Description

A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

m and n will be at most 100.

#### Example
##### Example 1:

    Input: n = 1, m = 3
    Output: 1

    Explanation: Only one path to target position.

##### Example 2:

    Input:  n = 3, m = 3
    Output: 6

    Explanation:
    	D : Down
    	R : Right
    	1) DDRR
    	2) DRDR
    	3) DRRD
    	4) RRDD
    	5) RDRD
    	6) RDDR


### Easy   111. Climbing Stairs
http://www.lintcode.com/problem/climbing-stairs/
https://leetcode.com/problems/climbing-stairs/

#### Description

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#### Example
##### Example 1:
		Input:  n = 3
		Output: 3

		Explanation:
		1) 1, 1, 1
		2) 1, 2
		3) 2, 1
		total 3.

##### Example 2:
		Input:  n = 1
		Output: 1

		Explanation:  
		only 1 way.


### Easy   110. Minimum Path Sum
http://www.lintcode.com/problem/minimum-path-sum/
https://leetcode.com/problems/minimum-path-sum/

#### Description

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

You can only go right or down in the path..

#### Example
##### Example 1:
	Input:  [[1,3,1],[1,5,1],[4,2,1]]
	Output: 7

	Explanation:
	Path is: 1 -> 3 -> 1 -> 1 -> 1

##### Example 2:
	Input:  [[1,3,2]]
	Output: 6

	Explanation:  
	Path is: 1 -> 3 -> 2


### Medium 603. Largest Divisible Subset
http://www.lintcode.com/problem/largest-divisible-subset/

#### Description

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

#### Example
##### Example 1:

  Input: nums =  [1,2,3],
  Output: [1,2] or [1,3]

##### Example 2:

  Input: nums = [1,2,4,8],
  Output: [1,2,4,8]

### Medium 611. Knight Shortest Path
https://www.lintcode.com/problem/knight-shortest-path/

### Medium 76. Longest Increasing Subsequence
https://www.lintcode.com/problem/longest-increasing-subsequence/
https://leetcode.com/problems/longest-increasing-subsequence/

#### Description

Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

#### Clarification

What's the definition of longest increasing subsequence?

The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

https://en.wikipedia.org/wiki/Longest_increasing_subsequence

#### Example
##### Example 1:
	Input:  [5,4,1,2,3]
	Output:  3

	Explanation:
	LIS is [1,2,3]


#### Example 2:
	Input: [4,2,4,5,3,7]
	Output:  4

	Explanation:
	LIS is [2,4,5,7]

#### Challenge
  Time complexity O(n^2) or O(nlogn)

### Hard   602. Russian Doll Envelopes
https://www.lintcode.com/problem/russian-doll-envelopes

#### Description

Give a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
Find the maximum number of nested layers of envelopes.

#### Example
##### Example 1:

    Input：[[5,4],[6,4],[6,7],[2,3]]
    Output：3
    Explanation：
    the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

##### Example 2:

    Input：[[4,5],[4,6],[6,7],[2,3],[1,1]]
    Output：4
    Explanation：
    the maximum number of envelopes you can Russian doll is 4 ([1,1] => [2,3] => [4,5] / [4,6] => [6,7]).


## Optional (4)

### Easy   272. Climbing Stairs II
https://www.lintcode.com/problem/climbing-stairs-ii/

#### Description

A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

#### Clarification
For n=0, we think the answer is 1.

#### Example
##### Example 1:

		Input: 3
		Output: 4
		Explanation: 1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3 , there are 4 ways.
##### Example 2:

		Input: 4
		Output: 7
		Explanation: 1 + 1 + 1 + 1 = 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 2 + 2 = 1 + 3 = 3 + 1 = 4 , there are 7 ways.


### Medium 117. Jump Game II
https://www.lintcode.com/problem/jump-game-ii/

### Medium 116. Jump Game
https://www.lintcode.com/problem/jump-game/

### Hard   622. Frog Jump
https://www.lintcode.com/problem/frog-jump/

## Related (3)

### Easy   254. Drop Eggs
https://www.lintcode.com/problem/drop-eggs/

### Medium 630. Knight Shortest Path II
https://www.lintcode.com/problem/knight-shortest-path-ii/

### Medium 584. Drop Eggs II
https://www.lintcode.com/problem/drop-eggs-ii/


## ==========================================

### 669. Coin Change
https://www.lintcode.com/problem/coin-change/
https://leetcode.com/problems/coin-change/

#### Description

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

		You may assume that you have an infinite number of each kind of coin.

#### Example
##### Example1

		Input:
		[1, 2, 5]
		11
		Output: 3
		Explanation: 11 = 5 + 5 + 1
##### Example2

		Input:
		[2]
		3
		Output: -1
