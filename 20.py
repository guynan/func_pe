# identical to 16
f = lambda n: 1 if n == 0 else n * f(n - 1);
pds = lambda n: sum(int(x) for x in str(n));
print(pds(f(100)));
