# 8 - Data Structure - Stack, Queue, Hash, Heap

## Required

### Easy  642. Moving Average from Data Stream
https://www.lintcode.com/problem/moving-average-from-data-stream

#### Description
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

#### Example
    MovingAverage m = new MovingAverage(3);
    m.next(1) = 1 // return 1.00000
    m.next(10) = (1 + 10) / 2 // return 5.50000
    m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
    m.next(5) = (10 + 3 + 5) / 3 // return 6.00000

### Easy  494. Implement Stack by Two Queues
https://www.lintcode.com/problem/implement-stack-by-two-queues

#### Description
Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

#### Example
    push(1)
    pop()
    push(2)
    isEmpty() // return false
    top() // return 2
    pop()
    isEmpty() // return true

### Easy  209. First Unique Character in a String
https://www.lintcode.com/problem/first-unique-character-in-a-string

#### Description
Find the first unique character in a given string. You can assume that there is at least one unique character in the string.

#### Example
For "abaccdeff", return 'b'.

#### Challenge
No extra storage is used.

### Medium  657. Insert Delete GetRandom O(1)
https://www.lintcode.com/problem/insert-delete-getrandom-o1

#### Description
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

#### Example
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

### Medium  612. K Closest Points
https://www.lintcode.com/problem/k-closest-points

#### Description
Given some points and an origin point in two-dimensional space, find k points which are nearest to the origin.
Return these points sorted by distance, if they are same in distance, sorted by the x-axis, and if they are same in the x-axis, sorted by y-axis.

#### Example
    Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
    return [[1,1],[2,5],[4,4]]

### Medium  544. Top k Largest Numbers
https://www.lintcode.com/problem/top-k-largest-numbers

#### Description
Given an integer array, find the top k largest numbers in it.

#### Example
Given [3,10,1000,-99,4,100] and k = 3.
Return [1000, 100, 10].

### Medium  104. Merge K Sorted Lists

### Medium  40. Implement Queue by Two Stacks
https://www.lintcode.com/problem/implement-queue-by-two-stacks

#### Description
As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

#### Example
    push(1)
    pop()     // return 1
    push(2)
    push(3)
    top()     // return 2
    pop()     // return 2

#### Challenge
implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by AVERAGE.

### Medium  4. Ugly Number II
### Hard  134. LRU Cache

## Optional

### Easy  495. Implement Stack
https://www.lintcode.com/problem/implement-stack

#### Description
Implement a stack. You can use any data structure inside a stack except stack itself to implement it.

#### Example
    push(1)
    pop()
    push(2)
    top()  // return 2
    pop()
    isEmpty() // return true
    push(3)
    isEmpty() // return false

### Easy  128. Hash Function
### Medium  685. First Unique Number In Stream
### Medium  613. High Five
### Medium  606. Kth Largest Element II
### Medium  601. Flatten 2D Vector
### Medium  545. Top k Largest Numbers II
### Medium  526. Load Balancer
### Medium  486. Merge K Sorted Arrays
### Medium  130. Heapify
### Medium  129. Rehashing
### Medium  124. Longest Consecutive Sequence

## Related

### Easy  551. Nested List Weight Sum
https://www.lintcode.com/problem/nested-list-weight-sum

#### Description
Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is either an integer, or a list -- whose elements may also be integers or other lists.

#### Example
    Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10)
    Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4 * 2 + 6 * 3 = 27)

> ### Easy  494. Implement Stack by Two Queues (same question)

### Medium  575. Decode String
### Medium  541. Zigzag Iterator II
### Medium  540. Zigzag Iterator
### Medium  528. Flatten Nested List Iterator
### Medium  471. Top K Frequent Words
### Medium  224. Implement Three Stacks by Single Array
### Hard  24. LFU Cache
