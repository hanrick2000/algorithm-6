# 01 - Interview Flow

## Required(1)

### Easy 9. Fizz Buzz
https://www.lintcode.com/problem/fizz-buzz/
https://leetcode.com/problems/fizz-buzz/

#### Description

Given number n. Print number from 1 to n. But:

* when number is divided by 3, print "fizz".
* when number is divided by 5, print "buzz".
* when number is divided by both 3 and 5, print "fizz buzz".
* when number can't be divided by either 3 or 5, print the number itself.

#### Example
    If n = 15, you should return:
    [
      "1", "2", "fizz",
      "4", "buzz", "fizz",
      "7", "8", "fizz",
      "buzz", "11", "fizz",
      "13", "14", "fizz buzz"
    ]

    If n = 10, you should return:
    [
      "1", "2", "fizz",
      "4", "buzz", "fizz",
      "7", "8", "fizz",
      "buzz"
    ]

#### Challenge
Can you do it with only one if statement?


### Easy 82. Single Number
https://www.lintcode.com/problem/single-number/
https://leetcode.com/problems/single-number/

#### Description

Given 2 * n + 1 numbers, every numbers occurs twice except one, find it.

    n≤100

#### Example
##### Example 1:

    Input：[1,1,2,2,3,4,4]
    Output：3
    Explanation:
    Only 3 appears once
##### Example 2:

    Input：[0,0,1]
    Output：1
    Explanation:
    Only 1 appears once

#### Challenge
One-pass, constant extra space.


### Easy 1038. Jewels And Stones
https://www.lintcode.com/problem/jewels-and-stones/
https://leetcode.com/problems/jewels-and-stones/

#### Description

You are given strings J representing the types of stones that are jewels, and S representing the stones you have. Each character in S is a type of stone you have. You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

    * S and J will consist of letters and have length at most 50.
    * The characters in J are distinct.

#### Example
##### Example 1:

    Input: J = "aA", S = "aAAbbbb"
    Output: 3
##### Example 2:

    Input: J = "z", S = "ZZ"
    Output: 0


### Easy 1535. To Lower Case
https://www.lintcode.com/problem/to-lower-case/
https://leetcode.com/problems/to-lower-case/

#### Description

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

#### Example
##### Example 1:

    Input: "Hello"
    Output: "hello"
##### Example 2:

    Input: "here"
    Output: "here"
##### Example 3:

    Input: "LOVELY"
    Output: "lovely"


### Easy 175. Invert Binary Tree
https://www.lintcode.com/problem/invert-binary-tree/
https://leetcode.com/problems/invert-binary-tree/

#### Description

Invert a binary tree.Left and right subtrees exchange.

#### Example
##### Example 1:

    Input: {1,3,#}
    Output: {1,#,3}
    Explanation:
    	  1    1
    	 /  =>  \
    	3        3
##### Example 2:

    Input: {1,2,3,#,#,4}
    Output: {1,3,2,#,4}
    Explanation:

          1         1
         / \       / \
        2   3  => 3   2
           /       \
          4         4

#### Challenge
Do it in recursion is acceptable, can you do it without recursion?


### Easy 1236. Find All Numbers Disappeared in an Array
https://www.lintcode.com/problem/find-all-numbers-disappeared-in-an-array/
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

#### Description

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

#### Example
    Input:
    [4,3,2,7,8,2,3,1]
    Output:
    [5,6]
