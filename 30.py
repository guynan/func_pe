
sum5pow = lambda i: sum(int(c)** 5 for c in str(i));
g = lambda n, f: sum(x for x in range(10, n) if x == f(x))
print(g(10000000, sum5pow));
