for a in range(1,1000):
    for n in range(1,1000):
        if a**2-1 % n ==0 and (a-1 %n != 0 or a+1 %n != 0): print(a,n)