# Arithmetic Operators
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)


# Comparison Operators
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# Logical Operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)


# Assignment Operators
a = 10
a += 5
print(a)
a -= 5
print(a)
a *= 5
print(a)
a <<= 1
print(a)
a >>= 1
print(a)

# Ternary Operator
a, b = 10, 20
min = a if a < b else b
print(min)