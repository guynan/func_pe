

f = lambda n: 1 if n == 0 else n * f(n - 1);
sf = lambda n: sum(f(int(x)) for x in str(n));
print(sum([x for x in range(3, 50000) if sf(x) == x]));
