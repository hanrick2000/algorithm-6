# 2 - Breadth First Search

## Required (10)

### Easy  433. Number of Islands
https://www.lintcode.com/problem/number-of-islands/

#### Description

Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

#### Example
##### Example 1:

    Input:
    [
      [1,1,0,0,0],
      [0,1,0,0,1],
      [0,0,0,1,1],
      [0,0,0,0,0],
      [0,0,0,0,1]
    ]
    Output:
    3
##### Example 2:

    Input:
    [
      [1,1]
    ]
    Output:
    1

### Easy  69. Binary Tree Level Order Traversal
https://www.lintcode.com/problem/binary-tree-level-order-traversal/

#### Description

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

* The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
* The number of nodes does not exceed 20.

#### Example
##### Example 1:

    Input：{1,2,3}
    Output：[[1],[2,3]]
    Explanation：
      1
     / \
    2   3
    it will be serialized {1,2,3}
    level order traversal
##### Example 2:

    Input：{1,#,2,3}
    Output：[[1],[2],[3]]
    Explanation：
    1
     \
      2
     /
    3
    it will be serialized {1,#,2,3}
    level order traversal

#### Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use BFS algorithm to do it.


### Medium  615. Course Schedule
https://www.lintcode.com/problem/course-schedule/

#### Description

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

#### Example
##### Example 1:

    Input: n = 2, prerequisites = [[1,0]]
    Output: true
##### Example 2:

    Input: n = 2, prerequisites = [[1,0],[0,1]]
    Output: false


### Medium  616. Course Schedule II
https://www.lintcode.com/problem/course-schedule-ii/

#### Description

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

#### Example
##### Example 1:

    Input: n = 2, prerequisites = [[1,0]]
    Output: [0,1]
##### Example 2:

    Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,1,2,3] or [0,2,1,3]


### Medium  611. Knight Shortest Path
https://www.lintcode.com/problem/knight-shortest-path/

#### Description

Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.

Return -1 if destination cannot be reached.

    source and destination must be empty.
    Knight can not enter the barrier.
    Path length refers to the number of steps the knight takes.

#### Clarification
If the knight is at (x, y), he can get to the following positions in one step:

    (x + 1, y + 2)
    (x + 1, y - 2)
    (x - 1, y + 2)
    (x - 1, y - 2)
    (x + 2, y + 1)
    (x + 2, y - 1)
    (x - 2, y + 1)
    (x - 2, y - 1)
#### Example
##### Example 1:

    Input:
    [[0,0,0],
     [0,0,0],
     [0,0,0]]
    source = [2, 0] destination = [2, 2]
    Output: 2
    Explanation:
    [2,0]->[0,1]->[2,2]
#### Example 2:

    Input:
    [[0,1,0],
     [0,0,1],
     [0,0,0]]
    source = [2, 0] destination = [2, 2]
    Output:-1


### Medium  605. Sequence Reconstruction
https://www.lintcode.com/problem/sequence-reconstruction/

#### Description

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 10^4. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

#### Example
##### Example 1:

    Input:org = [1,2,3], seqs = [[1,2],[1,3]]
    Output: false
    Explanation:
    [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
##### Example 2:

    Input: org = [1,2,3], seqs = [[1,2]]
    Output: false
    Explanation:
    The reconstructed sequence can only be [1,2].
##### Example 3:

    Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
    Output: true
    Explanation:
    The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
##### Example 4:

    Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
    Output:true


### Medium  137. Clone Graph
https://www.lintcode.com/problem/clone-graph/

#### Description

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

    You need return the node with the same label as the input node.

#### Clarification
How we serialize an undirected graph: http://www.lintcode.com/help/graph/

#### Example
##### Example1

    Input:
    {1,2,4#2,1,4#4,1,2}
    Output:
    {1,2,4#2,1,4#4,1,2}
    Explanation:
    1------2  
     \     |  
      \    |  
       \   |  
        \  |  
          4   


### Medium  127. Topological Sorting
https://www.lintcode.com/problem/topological-sorting/

#### Description
Given an directed graph, a topological order of the graph nodes is defined as follow:

* For each directed edge A -> B in graph, A must before B in the order list.
* The first node in the order can be any node in the graph with no nodes direct to it.

Find any topological order for the given graph.

    You can assume that there is at least one topological order in the graph.

#### Clarification
Learn more about representation of graphs

#### Example
For graph as follow:

##### picture

![Topological Sorting](https://github.com/porrychen/algorithm/blob/master/2%20-%20Breadth%20First%20Search/127.%20Topological%20Sorting.jpeg)

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...

#### Challenge
Can you do it in both BFS and DFS?


### Medium  7. Serialize and Deserialize Binary Tree
https://www.lintcode.com/problem/serialize-and-deserialize-binary-tree/

#### Description

Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

    There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.

#### Example
##### Example 1:

    Input：{3,9,20,#,#,15,7}
    Output：{3,9,20,#,#,15,7}
    Explanation：
    Binary tree {3,9,20,#,#,15,7},  denote the following structure:
    	  3
    	 / \
    	9  20
    	  /  \
    	 15   7
    it will be serialized {3,9,20,#,#,15,7}
##### nExample 2:

    Input：{1,2,3}
    Output：{1,2,3}
    Explanation：
    Binary tree {1,2,3},  denote the following structure:
       1
      / \
     2   3
    it will be serialized {1,2,3}

Our data serialization use BFS traversal. This is just for when you got Wrong Answer and want to debug the input.

You can use other method to do serialization and deserialization.


### Hard  120. Word Ladder
https://www.lintcode.com/problem/word-ladder/

#### Description

Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that:

1. Only one letter can be changed at a time

2. Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )

*  Return 0 if there is no such transformation sequence.
* All words have the same length.
* All words contain only lowercase alphabetic characters.
* You may assume no duplicates in the word list.
* You may assume beginWord and endWord are non-empty and are not the same.

#### Example
##### Example 1:

    Input：start = "a"，end = "c"，dict =["a","b","c"]
    Output：2
    Explanation：
    "a"->"c"
##### Example 2:

    Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
    Output：5
    Explanation：
    "hit"->"hot"->"dot"->"dog"->"cog"


## Optional (11)

### Easy  242. Convert Binary Tree to Linked Lists by Depth
https://www.lintcode.com/problem/convert-binary-tree-to-linked-lists-by-depth/

#### Description

Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

#### Example
##### Example 1:

    Input: {1,2,3,4}
    Output: [1->null,2->3->null,4->null]
    Explanation:
            1
           / \
          2   3
         /
        4
##### Example 2:

    Input: {1,#,2,3}
    Output: [1->null,2->null,3->null]
    Explanation:
        1
         \
          2
         /
        3


### Medium  624. Remove Substrings
https://www.lintcode.com/problem/remove-substrings/

#### Description

Given a string s and a set of n substrings. You are supposed to remove every instance of those n substrings from s so that s is of the minimum length and output this minimum length.

#### Example
##### Example 1:

    Input:
    "ccdaabcdbb"
    ["ab","cd"]
    Output:
    2
    Explanation:
    ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)
##### Example 2:

    Input:
    "abcabd"
    ["ab","abcd"]
    Output:
    0
    Explanation:
    abcabd -> abcd -> "" (length = 0)


### Medium  618. Search Graph Nodes
https://www.lintcode.com/problem/search-graph-nodes/

#### Description

Given an undirected graph, a node and a target, return the nearest node to given node which value of it is target, return NULL if you can't find.

There is a mapping store the nodes' values in the given parameters.

    It's guaranteed there is only one available solution

#### Example
##### Example 1:

    Input:
    {1,2,3,4#2,1,3#3,1#4,1,5#5,4}
    [3,4,5,50,50]
    1
    50
    Output:
    4
    Explanation:
    2------3  5
     \     |  |
      \    |  |
       \   |  |
        \  |  |
          1 --4
    Give a node 1, target is 50

    there a hash named values which is [3,4,10,50,50], represent:
    Value of node 1 is 3
    Value of node 2 is 4
    Value of node 3 is 10
    Value of node 4 is 50
    Value of node 5 is 50

    Return node 4
##### Example 2:

    Input:
    {1,2#2,1}
    [0,1]
    1
    1
    Output:
    2


### Medium  598. Zombie in Matrix
https://www.lintcode.com/problem/zombie-in-matrix/

#### Description

Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

#### Example
##### Example 1:

    Input:
    [[0,1,2,0,0],
     [1,0,0,2,1],
     [0,1,0,0,0]]
    Output:
    2
##### Example 2:

    Input:
    [[0,0,0],
     [0,0,0],
     [0,0,1]]
    Output:
    4


### Medium  531. Six Degrees
https://www.lintcode.com/problem/six-degrees/

#### Description

Six degrees of separation is the theory that everyone and everything is six or fewer steps away, by way of introduction, from any other person in the world, so that a chain of "a friend of a friend" statements can be made to connect any two people in a maximum of six steps.

Given a friendship relations, find the degrees of two people, return -1 if they can not been connected by friends of friends.

#### Example
##### Example1

    Input: {1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4
    Output: 2
    Explanation:
        1------2-----4
         \          /
          \        /
           \--3--/
##### Example2

    Input: {1#2,4#3,4#4,2,3} and s = 1, t = 4
    Output: -1
    Explanation:
        1      2-----4
                     /
                   /
                  3


### Medium  178. Graph Valid Tree
https://www.lintcode.com/problem/graph-valid-tree/

#### Description

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

    You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

#### Example
##### Example 1:

    Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    Output: true.
##### Example 2:

    Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    Output: false.


### Medium  431. Connected Component in Undirected Graph
https://www.lintcode.com/problem/connected-component-in-undirected-graph/

### Medium  71. Binary Tree Zigzag Level Order Traversal
https://www.lintcode.com/problem/binary-tree-zigzag-level-order-traversal/

### Medium  70. Binary Tree Level Order Traversal II
https://www.lintcode.com/problem/binary-tree-level-order-traversal-ii/

### Hard  794. Sliding Puzzle II
https://www.lintcode.com/problem/sliding-puzzle-ii/

### Hard  573. Build Post Office II
https://www.lintcode.com/problem/build-post-office-ii/

## Related (3)

### Medium  434. Number of Islands II
https://www.lintcode.com/problem/number-of-islands-ii/

### Hard  600. Smallest Rectangle Enclosing Black Pixels
https://www.lintcode.com/problem/smallest-rectangle-enclosing-black-pixels/

### Hard  574. Build Post Office
https://www.lintcode.com/problem/build-post-office/
