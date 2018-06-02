
prime = lambda n: [] == [0 for x in range(3, int(ceil(sqrt(n))), 2) if n % x == 0]

isp = lambda i: "123456789" == str(i);
rn = range(987654321, 123456789, -1);
print(max([x for x in rn 
