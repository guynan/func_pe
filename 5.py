from itertools import count;

divis = lambda i, n: [] == [1 for x in range(1, n +1) if i % x != 0];
rn = range(1,250000000);
g = lambda n: min([x for x in rn if divis(x, n)]);
print(g(20));
