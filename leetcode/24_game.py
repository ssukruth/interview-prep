"""
You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.



Example 1:

Input: cards = [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24
Example 2:

Input: cards = [1,2,1,2]
Output: false
"""


class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        n = len(cards)

        # If you have only one card then see if the card evaluates to 24
        if n == 1:
            if abs(cards[0] - 24) < 0.0001: # This 0.0001 check is required due to floating point division issues
                return True
            return False

        for i in range(n):
            for j in range(i+1, n):
                c1 = cards[i]
                c2 = cards[j]

                # get 2 cards from the deck
                # check possible values generated from them
                possible_combinations = [c1+c2, c1-c2, c2-c1, c1*c2]

                if c1 != 0:
                    possible_combinations.append(float(c2)/c1)
                if c2 != 0:
                    possible_combinations.append(float(c1)/c2)

                # Remove the original cards as we'll use the value of operation performed on them to proceed further
                cards.remove(c1)
                cards.remove(c2)

                # For each possible value, add the value to the new deck and check if new deck evaluates to True
                for c in possible_combinations:
                    if self.judgePoint24([c] + cards):
                        return True

                # Add the cards back to their original pos (backtracking)
                cards.insert(i, c1)
                cards.insert(j, c2)

        return False
