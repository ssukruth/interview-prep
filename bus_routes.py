"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.



Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1


Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
"""

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """

        # Treat routes as nodes. There is an edge between two routes if they share a common bus stop

        from collections import defaultdict, deque
        # Map stops with busses
        bus_map = defaultdict(set)

        for i, route in enumerate(routes):
            for bus_stop in route:
                bus_map[bus_stop].add(i)


        visited = set()
        q = deque()
        q.append(source)
        level = 0

        # Perform a topological sort to figure out the distance between source and target
        while q:
            for _ in range(len(q)):
                bus_stop = q.popleft()
                if bus_stop == target:
                    return level
                for bus in bus_map[bus_stop]:
                    if bus not in visited:
                        for stop in routes[bus]:
                            q.append(stop)
                    visited.add(bus)
            level += 1

        return -1

"""
Create a graph with bus_stop->route as edge
start the q at source bus stop
init level = 0
while q:
    for _ in range(len(q)):
        pop bus stop
        if bus stop is same as target:
            return level
        for route in graph[bus]:
            if route is not visited:
                for bus_stop in routes[route]:
                    q.append(bus_stop)
            mark route as visited
    level += 1
return -1
"""
