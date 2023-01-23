x = [[1,-3,2],[-8,5],[-1,-4,-3]]
delete_minus = lambda x:[[int(i) for i in inner if i>= 0] for inner in x]
print(delete_minus(x))

# def delete_minus(x):
#     return [[int(i) for i in inner if i>=0] for inner in x]
# print(delete_minus(x))