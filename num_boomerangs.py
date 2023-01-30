"""
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

 

Example 1:

Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: 2
Example 3:

Input: points = [[1,1]]
Output: 0
"""

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        if len(points) < 3:
            return 0

        def distance(x1, y1, x2, y2):
            return (x1-x2)**2 + (y1-y2)**2

        count = 0
        for point1 in points:
            dist_map = defaultdict(int)
            for point2 in points:
                if point1 == point2:
                    continue
                dist = distance(point1[0], point1[1], point2[0], point2[1])
                dist_map[dist] += 1

            for _, dist in dist_map.items():
                count += (dist * (dist-1))

        return count
