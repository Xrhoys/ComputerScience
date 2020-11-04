# Given a sorted array
arr = [1, 2, 4, 6, 7, 8, 9, 10, 476, 499, 678]

# Rushed / Proposition

def search(list, upper, lower, target):
  current = (upper + lower)//2

  if upper - lower < 1:
    return -1

  if len(list[lower: upper]) == 1:
    if list[current] != target:
      return -1
    else:
      return current

  if list[current] == target:
    return current
  elif list[current] > target:
    return search(list, current, lower, target)
  elif list[current] < target:
    return search(list, upper, current, target)

print(search(arr, len(arr) - 1, 0, 1))