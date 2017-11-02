
rn = range(2, 101);
dp = lambda: len({a ** b for a in rn for b in rn});
print(dp());
