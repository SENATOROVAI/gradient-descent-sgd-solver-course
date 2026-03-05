def mse(xs, ys, w, b):
    n = len(xs)
    s = 0.0
    for x, y in zip(xs, ys):
        e = (w * x + b) - y
        s += e * e
    return s / n

def update_batch(xs, ys, w, b, lr):
    m = len(xs)
    sw = 0.0
    sb = 0.0
    for x, y in zip(xs, ys):
        e = (w * x + b) - y
        sw += e * x
        sb += e
    w -= lr * (2.0 * sw / m)
    b -= lr * (2.0 * sb / m)
    return w, b

mode, n, batch_size, epochs = map(int, input().split())
xs = []
ys = []
for _ in range(n):
    x, y = map(float, input().split())
    xs.append(x)
    ys.append(y)
w, b, lr = map(float, input().split())

for _ in range(epochs):
    if mode == 0:
        w, b = update_batch(xs, ys, w, b, lr)
    elif mode == 1:
        i = 0
        while i < n:
            j = min(i + batch_size, n)
            w, b = update_batch(xs[i:j], ys[i:j], w, b, lr)
            i = j
    else:
        for x, y in zip(xs, ys):
            e = (w * x + b) - y
            w -= lr * (2.0 * e * x)
            b -= lr * (2.0 * e)

print('{:.6f} {:.6f} {:.6f}'.format(w, b, mse(xs, ys, w, b)))
