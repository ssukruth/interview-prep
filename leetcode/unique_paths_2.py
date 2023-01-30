"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result= {}

        def dfs(i, j, visited):
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in result:
                return result[(i, j)]
            count = 0
            if (i, j) not in visited:
                visited.add((i, j))
                for ii, jj in [[i, j+1], [i+1, j]]:
                    if ii >= m or jj >= n:
                        continue
                    if (ii, jj) in visited:
                        continue
                    if obstacleGrid[ii][jj] != 0:
                        continue
                    count += dfs(ii, jj, visited)
                visited.remove((i, j))
            result[(i, j)] = count
            return count

        if obstacleGrid[0][0] != 0:
            return 0
        return dfs(0, 0, set())
