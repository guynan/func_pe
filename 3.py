from math import sqrt, ceil;

prime = lambda n: [] == [0 for x in range(3, int(ceil(sqrt(n))), 2) if n % x == 0]
primef = lambda n, x: n % x == 0 and prime(x);
pf = lambda n: max([x for x in range(2, int(sqrt(n)) + 1) if primef(n, x)]);
print(pf(600851475143));
