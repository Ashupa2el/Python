import math
a, b = map(float,input().split(','))
c = float(input())

power = math.pow(a,b)
sqrtt = math.sqrt(c)

print(f"{power:.6f}\n{sqrtt:.6f}")
