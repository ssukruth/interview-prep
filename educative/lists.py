### Remove even elements from a list ###

def remove_even(lst):
    # Write your code here!
    newlst = []
    for item in lst:
        if item % 2 != 0:
            newlst.append(item)
    return newlst


### Merge two sorted lists ###

def merge_lists(lst1, lst2):
    # Write your code here
    merged = []
    c1, c2 = 0, 0

    while c1 < len(lst1) and c2 < len(lst2):
        if lst1[c1] < lst2[c2]:
            merged.append(lst1[c1])
            c1 += 1
        else:
            merged.append(lst2[c2])
            c2 += 1

    while c1 < len(lst1):
        merged.append(lst1[c1])
        c1 +=  1

    while c2 < len(lst2):
        merged.append(lst2[c2])
        c2 += 1

    return merged

### Find two numbers whose sum add upto k (two sum) ###

def find_sum(lst, k):
    # Write your code here
    s = set()

    for num in lst:
        if num in s:
            return [num, k - num]
        s.add(k - num)
    return [None, None]


### Update list with product of all items except the current item in the list ###

def find_product(lst):
    # Write your code here
    left = 1
    product = []
    # for each index, get product of all items to the left of it
    for ele in lst:
        product.append(left)
        left = left * ele
    print(product)
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product

### min val in a list ###

def find_minimum(arr):
    # Write your code here
    return min(arr)


### Second max value in a list ###

def find_second_maximum(lst):
    # Write your code here
    lst.remove(max(lst))
    return max(lst)


### Right rotate a list by k times ###

def right_rotate(lst, k):
    # Write your code here
    n = len(lst)
    k = k % n
    return lst[n-k:] + lst[0:n-k]

### Rearrange positive and negateive ###

def rearrange(lst):
    # Write your code here
    neg = [item for item in lst if item < 0]
    pos = [item for item in lst if item >= 0]
    return neg + pos

### Rearrange list in max min form ###

def max_min(lst):
    # Write your code here
    ret = []
    start, end = 0, len(lst) - 1
    append_max = True
    while len(ret) != len(lst):
        if append_max:
            ret.append(lst[end])
            end -= 1
        else:
            ret.append(lst[start])
            start += 1
        append_max = not append_max
    return ret


### Max sum sublist ###

def find_max_sum_sublist(lst):
  # Write your code here!
  T = [0] * len(lst)
  T[0] = lst[0]

  for ii in range(1, len(lst)):
    T[ii] = max(lst[ii], lst[ii] + T[ii -1])

  return max(T)

### Max sum sublist - Kadane's algo with O(1) space ###

def find_max_sum_sublist(lst):
  # Write your code here!
  max_sum  = lst[0]
  curr_sum = lst[0]

  for ii in range(1, len(lst)):
    if curr_sum < 0:
        curr_sum = lst[ii]
    else:
        curr_sum += lst[ii]

    max_sum = max(max_sum, curr_sum)

  return max_sum
