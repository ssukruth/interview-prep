"""
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

def fruits_into_baskets(fruits):
    start, end = 0, 0
    max_fruits, curr_fruits = 0, 0
    baskets = {}

    while end < len(fruits):
        if fruits[end] not in baskets:
            baskets[fruits[end]] = 0
        baskets[fruits[end]] += 1
        curr_fruits += 1
        while len(baskets) > 2:
            baskets[fruits[start]] -= 1
            curr_fruits -= 1
            if baskets[fruits[start]] == 0:
                baskets.pop(fruits[start])
            start += 1
        max_fruits = max(max_fruits, curr_fruits)
        end += 1
    return max_fruits

"""
- start with empty window, start=end=0
- maintain a dict of buckets where key is fruit type
- until end reaches end of list:
    - add an item to fruit bucket
    - while len of fruit buckets is > 2: shrink the window
    - check and set max fruits var
    - increment end
"""
