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
w0, b0, lr = map(float, input().split())

sw = 0.0
sb = 0.0
for x, y in zip(xs, ys):
    e = (w0 * x + b0) - y
    sw += e * x
    sb += e

w_batch = w0 - lr * (2.0 * sw / n)
b_batch = b0 - lr * (2.0 * sb / n)

w_sgd = w0
b_sgd = b0
for x, y in zip(xs, ys):
    e = (w_sgd * x + b_sgd) - y
    w_sgd -= lr * (2.0 * e * x)
    b_sgd -= lr * (2.0 * e)

print('{:.6f} {:.6f}'.format(mse(xs, ys, w_batch, b_batch), mse(xs, ys, w_sgd, b_sgd)))
