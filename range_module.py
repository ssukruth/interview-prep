"""
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
 

Example 1:

Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)


Constraints:

1 <= left < right <= 109
At most 104 calls will be made to addRange, queryRange, and removeRange.
"""

from bisect import bisect_left, bisect_right


class RangeModule(object):

    def __init__(self):
        self.intervals = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        # O(N) to add

        # Intervals stores data as [start1, end1, start2, end2, ..]
        # Fetch where left & right can go into the intervals list using bisect: O(logN)
        l = bisect_left(self.intervals, left)
        r = bisect_right(self.intervals, right)

        # If left index is odd then it means the left value belongs to previous range (as it is less than end of previous range)
        # Same goes for right index.

        # If left index is even then we need to add left value to the interval as it's not covered by existing ranges.
        # Same goes for right index.

        self.intervals[l:r] = [left] *(l%2==0) + [right] * (r%2==0)

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        # O(logN) to query

        # For every number between left -> right-1 to be in the same range:
        # For left you need to do a bisect right
        # For right you need to do a bisect left
        # This is because we need to ensure left is part of an existing range and right isn't.
        # When we query for left & right we should get the same index
        # The index should be odd i.e. it's covered by previous range

        l = bisect_right(self.intervals, left)
        r = bisect_left(self.intervals, right)
        return l == r and l % 2 == 1


    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        # O(N) to remove

        # Remove range is the exact opposite as add.
        l = bisect_left(self.intervals, left)
        r = bisect_right(self.intervals, right)
        # So we remove left and right if they're odd indices in the array
        self.intervals[l:r] = [left] *(l%2==1) + [right] * (r%2==1)
