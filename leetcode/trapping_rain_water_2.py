"""
407. Trapping Rain Water II
Hard

2967

71

Add to List

Share
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.



Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
"""

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        from heapq import *
        q = []
        m, n = len(heightMap), len(heightMap[0])
        seen = set()

        # Start closing in from the boundaries.
        # Fetch the smallest boundary (this is why we need min heap) & compare it's adjacent cell
        # If height of adj cell < boundary:
        #       we can fill water
        # Else:
        #       adj cell becomes the new boundary
        for i in range(m):
            for j in range(n):
                if i in [0, m - 1] or j in [0, n - 1]:
                    heappush(q, (heightMap[i][j], i, j))
                    seen.add((i, j))

        water = 0

        while q:
            h, i, j = heappop(q)
            for ii, jj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if ii < 0 or jj < 0 or ii >= m or jj >= n:
                    continue
                if (ii, jj) in seen:
                    continue
                seen.add((ii, jj))
                boundary = max(h, heightMap[ii][jj])
                water += boundary - heightMap[ii][jj]
                heappush(q, (boundary, ii, jj))

        return water
