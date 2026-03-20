li = list(map(int, input().split()))

output = []

max = li[-1]
output.append(max)
for i in range(len(li)-2,-1,-1):
    if max < li[i]:
        max = li[i]
        output.append(max)
print(output[::-1])