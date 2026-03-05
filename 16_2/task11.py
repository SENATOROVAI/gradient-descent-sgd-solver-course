n = int(input().strip())
xs = []
ys = []
for _ in range(n):
    x, y = map(float, input().split())
    xs.append(x)
    ys.append(y)
w, b, lr = map(float, input().split())

for x, y in zip(xs, ys):
    e = (w * x + b) - y
    w -= lr * (2.0 * e * x)
    b -= lr * (2.0 * e)

print('{:.6f} {:.6f}'.format(w, b))
