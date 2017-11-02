
isp = lambda x, y: str(x*y) == str(x*y)[::-1];
rn = lambda n: range(1, n);
pp = lambda n: max([x * y for x in rn(n) for y in rn(n) if isp(x, y)]);

print(pp(1000));


