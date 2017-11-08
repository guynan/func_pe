
ismult = lambda x: x % 3 == 0 or x % 5 == 0;
mult35 = lambda n: sum(filter(ismult, [x for x in range(n)]));
print(mult35(1000));
