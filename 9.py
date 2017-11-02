

ispythag = lambda a, b, c: c **2 == a**2 + b**2;

sumtrip = lambda a, b, c, tot: tot == (a + b + c);
rn = range(1001);
cond = lambda a, b, c, i: a < b < c and sumtrip(a, b, c, i) and ispythag(a,b,c);
spec = lambda i: [a*b*c for a in rn for b in rn for c in rn if cond(a,b,c,i)];


print(sum(spec(1000)))
