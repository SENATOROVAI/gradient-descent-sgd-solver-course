import random

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

n, batch_size, seed = map(int, input().split())
xs = []
ys = []
for _ in range(n):
    x, y = map(float, input().split())
    xs.append(x)
    ys.append(y)
w, b, lr = map(float, input().split())

idx = list(range(n))
rnd = random.Random(seed)
rnd.shuffle(idx)
shx = [xs[i] for i in idx]
shy = [ys[i] for i in idx]

i = 0
while i < n:
    j = min(i + batch_size, n)
    w, b = update_batch(shx[i:j], shy[i:j], w, b, lr)
    i = j

print('{:.6f} {:.6f}'.format(w, b))
