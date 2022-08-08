m=3
n=2
A= {x if x%m==0 else None for x in range(100)}
A.remove(None)
B= {x if x%n==0 else None for x in range(100)}
B.remove(None)
C= {x if x%(m*n)==0 else None for x in range(100)}
C.remove(None)

print(C)
print(A.intersection(B))