

div = lambda i: [x for x in range(1, i) if i % x == 0]
abund = lambda n: n > sum(div(n));
rn = range(1, 28123)

a = [x for x in rn if abund(x)]
na = [x for x in rn if abund(x)]

print(sum({x + y for x in rn for y in rn}) - sum({x + y for x in a for y in a}));
