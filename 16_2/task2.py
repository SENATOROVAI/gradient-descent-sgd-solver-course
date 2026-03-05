w, b, x, y = map(float, input().split())
e = (w * x + b) - y
print('{:.6f}'.format(e * e))
