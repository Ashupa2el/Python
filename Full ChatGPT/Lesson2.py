n = int(input('Enter a number '))
fact = 1
if n < 0:
    print("Not defined")
else:
    while n>1:
        fact = fact * n
        n -= 1
        print(fact)