"""
isalpha => check for alpha
isdigit => check for digit
isalnum => check if it's alpha or digit
swapcase => returns new string with case changed
"""

"""
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""
def find_letter_case_string_permutations(str):
  permutations = []
  permutations.append(str)

  for i in range(len(str)):
    if str[i].isdigit():
      continue
    n = len(permutations)
    for j in range(n):
      p = list(permutations[j])
      p[i]= p[i].swapcase()
      permutations.append("".join(p))

  return permutations
