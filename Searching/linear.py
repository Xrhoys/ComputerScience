arr = [1, 3, 6, 7, 4, 6, 7, 0, 3, 4, 6, 1]

# Linear search algorithm, returns -1 if not found.
def search(target):
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
  return -1

print(search(4))