m = int(input().strip())
xs = []
ys = []
for _ in range(m):
    x, y = map(float, input().split())
    xs.append(x)
    ys.append(y)
w, b, lr = map(float, input().split())

sw = 0.0
sb = 0.0
for x, y in zip(xs, ys):
    e = (w * x + b) - y
    sw += e * x
    sb += e

w -= lr * (2.0 * sw / m)
b -= lr * (2.0 * sb / m)
print('{:.6f} {:.6f}'.format(w, b))
