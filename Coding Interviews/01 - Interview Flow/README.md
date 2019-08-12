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
