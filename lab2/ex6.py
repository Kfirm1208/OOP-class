x = [float(i) for i in input().split()]
y = [float(j) for j in input().split()]

add2list = lambda x,y:[x[i] + y[i] for i in range(len(x))]
print(add2list(x,y))
# result = [x_i + y_i for x_i, y_i in zip(x, y)]