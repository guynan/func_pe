from math import sqrt, ceil;

prime = lambda n: [] == [0 for x in range(3, int(ceil(sqrt(n))), 2) if n % x == 0]
psum = lambda n: sum(x for x in range(n) if prime(x));
print(psum(2000000));
