
ds = lambda i: sum(int(x) for x in str(i));
rn = range(100);
print(max(ds(a**b) for a in rn for b in rn));
