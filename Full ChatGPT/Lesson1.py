num = int(input('Enter any integer '))

if num % 2 == 0:
    if num > 0:
        print('Positive Even')
    elif num < 0:
        print('Negative Even')
    else:
        print('Zero')
else:
    if num > 0:
        print('Positive Odd')
    else:
        print('Negative Odd')