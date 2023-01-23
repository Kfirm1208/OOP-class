def count_minus(x):
    count = [i for i in x if i < 0]
    return len(count)
x = [int(j) for j in input().split()]
print(count_minus(x))

''' def count_minus(list1):
  return sum([i.count('-') for i in list1])
'''