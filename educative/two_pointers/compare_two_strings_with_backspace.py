"""
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example 1:

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
Example 2:

Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
Example 3:

Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
Example 4:

Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
"""
def get_next_valid_char_index(arg, i):
  count = 0
  while i >= 0:
    if arg[i] == "#":
      count += 1
    else:
      if count == 0:
        return i
      else:
        count -= 1
    i -= 1
  return i

def backspace_compare(str1, str2):
  idx1, idx2 = len(str1) - 1, len(str2) - 1
  while idx1 >=0 and idx2 >= 0:
    idx1 = get_next_valid_char_index(str1, idx1)
    idx2 = get_next_valid_char_index(str2, idx2)
    if idx1 < 0 and idx2 < 0:
        return True
    if idx1 < 0 or idx2 < 0:
      return False
    if str1[idx1] != str2[idx2]:
      return False
    idx1 -= 1
    idx2 -= 1
  return True
