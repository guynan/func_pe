
f = lambda i: sum(x**2 for x in range(i+1));
g = lambda i: sum(x for x in range(i+1)) ** 2;

ss = lambda x: g(x) - f(x);
print(ss(100));
