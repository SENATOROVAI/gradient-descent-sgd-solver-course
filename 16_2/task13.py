x, y, w, b, lr, beta, v_w, v_b = map(float, input().split())
e = (w * x + b) - y
g_w = 2.0 * e * x
g_b = 2.0 * e

v_w = beta * v_w + (1.0 - beta) * g_w
v_b = beta * v_b + (1.0 - beta) * g_b

w -= lr * v_w
b -= lr * v_b

print('{:.6f} {:.6f} {:.6f} {:.6f}'.format(w, b, v_w, v_b))
