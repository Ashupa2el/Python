li = list(map(int, input().split()))
sum = 0
for i in li:
    if i%2!=0:
        sum += i
if sum == 7:
    print(sum+-1)
else:
    print(sum)