n = int(input("Enter a number: "))

while n != 1 and n != 4:
    s = 0
    while n > 0:
        d = n % 10
        s = s + (d * d)
        n = n // 10
    n = s

if n == 1:
    print("True")
else:
    print("False")