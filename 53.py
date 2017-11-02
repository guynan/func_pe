
f = lambda n: 1 if n == 0 else n * f(n - 1);

ncr = lambda n, r: f(n) / (f(r)* f(n-r));
rn = range(1, 101);
print(len([1 for n in rn for r in rn if r <=n and ncr(n, r) > 1000000]));

