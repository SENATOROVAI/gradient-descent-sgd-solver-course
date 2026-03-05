x, g, lr = map(float, input().split())
x_new = x - lr * g
print('{:.6f}'.format(x_new))
