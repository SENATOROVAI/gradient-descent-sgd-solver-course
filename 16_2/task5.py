def batch_step(xs, ys, w, b, lr):
    n = len(xs)
    sw = 0.0
    sb = 0.0
    for x, y in zip(xs, ys):
        e = (w * x + b) - y
        sw += e * x
        sb += e
    w -= lr * (2.0 * sw / n)
    b -= lr * (2.0 * sb / n)
    return w, b

def mse(xs, ys, w, b):
    n = len(xs)
    s = 0.0
    for x, y in zip(xs, ys):
        e = (w * x + b) - y
        s += e * e
    return s / n

n = int(input().strip())
xs = []
ys = []
for _ in range(n):
    x, y = map(float, input().split())
    xs.append(x)
    ys.append(y)
w, b, lr, epochs = input().split()
w = float(w)
b = float(b)
lr = float(lr)
epochs = int(epochs)

for _ in range(epochs):
    w, b = batch_step(xs, ys, w, b, lr)

print('{:.6f} {:.6f} {:.6f}'.format(w, b, mse(xs, ys, w, b)))
