n = int(input().strip())
xs = []
ys = []
for _ in range(n):
    x, y = map(float, input().split())
    xs.append(x)
    ys.append(y)
w, b = map(float, input().split())

sw = 0.0
sb = 0.0
for x, y in zip(xs, ys):
    e = (w * x + b) - y
    sw += e * x
    sb += e

dw = 2.0 * sw / n
db = 2.0 * sb / n
print('{:.6f} {:.6f}'.format(dw, db))
