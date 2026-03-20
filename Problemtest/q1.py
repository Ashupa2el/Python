num = int(input())
c = []
# for i in range(1,num +1):
#     if i%5 == 0 and i%3 == 0:
#         c.append('FizzBuzz')
#     elif i%3 == 0:
#         c.append('Fizz')
#     elif i%5 == 0:
#         c.append('Buzz')
#     else:
#         c.append(str(i))
# print(c)

for i in range(1, num+1):
    c.append(str("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i))
print(c)