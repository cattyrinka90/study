# num = int(input())

# if 1000<= num <= 9999 and (num % 7 == 0 or num % 17 == 0):
#     print('YES')
# else:
#     print('NO')


# num1, num2, num3 = int(input()), int(input()), int(input())

# if (num1 + num2) > num3 and (num1 + num3) > num2 and (num2 + num3) > num1:
#     print('YES')
# else:
#     print('NO')

# a, b, c = int(input()), int(input()), int(input())
# p = (a + b + c) / 2

# if p > a and p > b and p > c:
#     print('YES')
# else:
#     print('NO')


year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('YES')
else :
    print('NO')