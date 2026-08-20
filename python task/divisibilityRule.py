# Divisible by 2
# n = int(input('Enter a number: '))
# last_digit = n%10 
# if last_digit in (0,2,4,6,8):
#     print('Divisible by 2')
# else:
#     print('Not Divisible by 2')


# Divisible by 3
# no = 15
# ones_place = no % 10  #5
# tens_place = no // 10 #1
# sum = ones_place + tens_place
# if sum%3 ==0:
#     print("Divisible by 3")


# Divisible by 4
# n = int(input("Enter a number: "))
# last_two = n % 100
# if last_two % 4 == 0:
#     print("Divisible by 4")
# else:
#     print("Not Divisible by 4")


# Divisible by 5
# n = int(input("Enter a number: "))
# last_digit = n % 10
# if last_digit == 0 or last_digit == 5:
#     print("Divisible by 5")
# else:
#     print("Not Divisible by 5")


# Divisible by 6
# n = int(input("Enter a number: "))
# if n % 2 == 0 and n % 3 == 0:
#     print("Divisible by 6")
# else:
#     print("Not Divisible by 6")


# Divisible by 8
# n = int(input("Enter a number: "))
# last_three = n % 1000
# if last_three % 8 == 0:
#     print("Divisible by 8")
# else:
#     print("Not Divisible by 8")


# Divisible by 9
# n = int(input("Enter a number: "))
# sum_digits = 0
# while n > 0:
#     digit = n % 10
#     sum_digits = sum_digits + digit
#     n = n // 10
# if sum_digits % 9 == 0:
#     print("Divisible by 9")
# else:
#     print("Not Divisible by 9")


# Divisible by 10
# n = int(input("Enter a number: "))
# last_digit = n % 10
# if last_digit == 0:
#     print("Divisible by 10")
# else:
#     print("Not Divisible by 10")


# Divisible by 11
n = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0
position = 1
while n > 0:
    digit = n % 10
    if position % 2 == 0:
        even_sum = even_sum + digit
    else:
        odd_sum = odd_sum + digit
    n = n // 10
    position += 1
difference = even_sum - odd_sum

if difference == 0 or difference % 11 == 0:
    print("Divisible by 11")
else:
    print("Not Divisible by 11")