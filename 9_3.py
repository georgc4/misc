
import math
def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

for p in range(1000):
    if is_prime(p) and is_prime(p+97):
        print(p)
print(is_prime(1013))