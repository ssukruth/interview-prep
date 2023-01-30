"""
Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
"""

def solve_knapsack(profits, weights, capacity):
  N = len(profits) # number of items
  W = capacity # max capacity

  T = [[0]*(N+1) for _ in range(W+1)]

  for w in range(W+1):
    for i in range(N+1):
      if weights[i-1] > w: # cannot fit item into the current sack
        T[w][i] = T[w][i-1]
      else: # can fit
        T[w][i] = max(
                        T[w][i-1], #without item
                        T[w-weights[i-1]][i-1] + profits[i-1] #with item
                    )
  return T[W][N]


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()

"""
T(w, i) = Profit using a knapsack of weight w & upto i items

when you cannot fit item i for weight w: T(w, i) = T(w, i-1)
when you can fit: T(w, i) = T(w-weights[i], i-1) + profit[i]
"""
