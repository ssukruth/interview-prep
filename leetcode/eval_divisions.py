"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        # Given that a/b = v, b/a = 1/v. Treat each a & b as nodes and add the weight as the value of the expression.
        # To find a/c given a/b & b/c we need to perform a/b * b/c
        # Therefore when we treat a, b, c as nodes and traverse from a to b we need to keep multiplying the values
        # The value seen at the end of the traversal when we see the second variable of the expression is the value for the expression

        from collections import defaultdict, deque

        graph = defaultdict(dict)

        for i, equation in enumerate(equations):
            x, y = equation
            val = values[i]
            graph[x][y] = val
            graph[y][x] = 1/val

        result = []
        for a, b in queries:
            if a not in graph or b not in graph:
                result.append(-1)
                continue

            val = -1
            seen = set()
            q = deque()

            if a in graph:
                q.append((a, 1))


            while q:
                x, v = q.popleft()
                if x == b:
                    val = v
                    break

                for y in graph[x]:
                    if y not in seen:
                        seen.add(y)
                        q.append((y, graph[x][y]*v))

            result.append(val)

        return result
