import math

# a, n = map(int, input('a, n: ').split())
a = 2
n = 1000
s = 0
for i in range(1, n+1):
    s += i * a ** (n - i)

print(s)
print((a*(a**n - n - 1) + n)/(a-1)**2)

