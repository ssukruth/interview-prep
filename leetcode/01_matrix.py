"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Ex1:
    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]

Ex2:
    Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque
        q = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j, 0))
                else:
                    mat[i][j] = -1

        while q:
            i, j, l = q.popleft()
            for (ii, jj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if ii < 0 or jj < 0 or ii >= len(mat) or jj >= len(mat[0]) or mat[ii][jj] != -1:
                    continue
                mat[ii][jj] = l + 1
                q.append((ii, jj, l+1))

        return mat

"""
- need like the shortest path to 0 so use BFS!
- build a q(i, j, 0) for all i,j where m(i,j) = 0
- set m(i, j) = -1 for all i, j where m(i,j) != 0
- while q:
    i, j, d = q.popleft()
    for r, c in all 4 dirs:
        boundary check and check if m(r, c) = -1
            m(r,c) = d+1
            add (r, c, d+1) to the q
"""
