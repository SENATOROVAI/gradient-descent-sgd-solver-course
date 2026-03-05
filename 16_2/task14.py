import math

x, y, w, lr, G = map(float, input().split())
e = (w * x) - y
g = 2.0 * e * x
G = G + g * g
w = w - lr * g / (math.sqrt(G) + 1e-8)

print('{:.6f} {:.6f}'.format(w, G))
