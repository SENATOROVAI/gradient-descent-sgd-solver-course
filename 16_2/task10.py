x, y, w, b, lr = map(float, input().split())
e = (w * x + b) - y
w -= lr * (2.0 * e * x)
b -= lr * (2.0 * e)
print('{:.6f} {:.6f}'.format(w, b))
